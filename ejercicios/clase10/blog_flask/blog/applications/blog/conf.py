BLOG_PREFIX_URL = "blog"

BLOG_LIST_URL_NAME = "blog_list"
BLOG_CREATE_URL_NAME = "blog_create"
BLOG_DETAIL_URL_NAME = "blog_detail"
BLOG_UPDATE_URL_NAME = "blog_update"
BLOG_DELETE_URL_NAME = "blog_delete"

def get_prefixed_url(url):
    return "{}.{}".format(BLOG_PREFIX_URL, url)