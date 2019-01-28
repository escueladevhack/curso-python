from pelican import signals
from pelican.readers import BaseReader, METADATA_PROCESSORS
from pelican.utils import  pelican_open
from markdown import Markdown
from markdown.extensions import meta as markdown_meta_preprocessor

import logging

logger = logging.getLogger(__name__)

# Create a new reader class, inheriting from the pelican.reader.BaseReader
class CustomMarkdownReader(BaseReader):
    enabled = True  # Yeah, you probably want that :-)

    # The list of file extensions you want this reader to match with.
    # If multiple readers were to use the same extension, the latest will
    # win (so the one you're defining here, most probably).
    file_extensions = ['md']

    def _parse_metadata(self, meta):
        """Return the dict containing document metadata"""
        formatted_fields = self.settings['FORMATTED_FIELDS']

        output = {}
        for name, value in meta.items():
            name = name.lower()
            if name in formatted_fields:
                # formatted metadata is special case and join all list values
                formatted_values = "\n".join(value)
                # reset the markdown instance to clear any state
                self._md.reset()
                formatted = self._md.convert(formatted_values)
                output[name] = self.process_metadata(name, formatted)
            elif name in METADATA_PROCESSORS:
                if len(value) > 1:
                    logger.warning(
                        'Duplicate definition of `%s` '
                        'for %s. Using first one.',
                        name, self._source_path)
                output[name] = self.process_metadata(name, value[0])
            elif len(value) > 1:
                # handle list metadata as list of string
                output[name] = self.process_metadata(name, value)
            else:
                # otherwise, handle metadata as single string
                output[name] = self.process_metadata(name, value[0])
        return output

    def read(self, source_path):
        """Parse content and metadata of markdown files"""

        self._source_path = source_path

        with pelican_open(source_path) as text:
            meta_preprocessor = markdown_meta_preprocessor.MetaPreprocessor(Markdown())
            lines = text.split("\n")
            lines = meta_preprocessor.run(lines)
            metadata = self._parse_metadata(meta_preprocessor.markdown.Meta)
            content = "\n".join(lines)

        return content, metadata

def add_reader(readers):
    readers.reader_classes['md'] = CustomMarkdownReader

# This is how pelican works.
def register():
    signals.readers_init.connect(add_reader)