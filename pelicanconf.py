#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Ricardo'
SITENAME = 'rb_dev'
SITEURL = 'http://spritkopf.github.io'
RELATIVE_URLS = True

PATH = 'content'

TIMEZONE = 'Europe/Berlin'
LOCALE = ('usa',  # On Windows
    'en_US',     # On Unix/Linux
    )

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('sdadsf','sdasdf'))

GITHUB_URL = 'http://github.com/spritkopf'

# Social widget
SOCIAL = (('GitHub', GITHUB_URL),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


# Specify name of a built-in theme
THEME = "pelican-clean-blog"


MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)



SITESUBTITLE = "Subtitle of the site...."

COLOR_SCHEME_CSS = 'monokai.css'
