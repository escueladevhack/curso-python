#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import sys

sys.path.append(os.path.dirname(
        os.path.abspath(__file__)
    )
)
from custom_pelican_markdown_reader.readers import CustomMarkdownReader

AUTHOR = 'Mauricio Collazos'
SITENAME = 'Curso rápido de Python'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Bogota'

DEFAULT_LANG = 'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = os.path.join(
    os.path.dirname(
        os.path.abspath(__file__)
    ),
    'themes',
    'remark'
)

READERS = {
    "md": CustomMarkdownReader
}

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
ARTICLE_ORDER_BY = "date"
PAGE_ORDER_BY = "date"