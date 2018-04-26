# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Evidlo'
SITENAME = 'UIUC Linux Users Group'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = "./themes/gnulug"

# Blogroll
# LINKS = (('Mailing List', 'http://getpelican.com/'),
#          ('Other place', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

MENUITEMS = (('Blog', '/blog/', 'fa fa-coffee'),
             ('Calendar', '/calendar', 'fa fa-calendar'),
             ('Wiki','/wiki/', 'fa fa-coffee'),
             ('Github','http://github.com/gnulug', 'fa fa-coffee'),
             ('About', '/about-us.html', 'fa fa-coffee'),
             ('Getting Help', '/getting-help.html', 'fa fa-coffee'),
             )
# MENUITEMS = (('Blog', '/blog/'),
#              ('Calendar', '/calendar'),
#              ('Wiki','/wiki/'),
#              ('Github','http://github.com/gnulug'),
#              ('About', '/about-us.html'),
#              ('Getting Help', '/getting-help.html'),
#              )

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)
SOCIAL = ()
FOUNDATION_FOOTER_TEXT = ' '

DEFAULT_PAGINATION = 10

PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['blog']
STATIC_PATHS = ['files', 'CNAME']
# STATIC_EXCLUDE_SOURCES = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

INDEX_URL = 'blog/'
INDEX_SAVE_AS = 'blog/index.html'
ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
CATEGORY_URL = 'category/{slug}.html'
CATEGORY_SAVE_AS = 'category/{slug}.html'

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
DISPLAY_LINKS_ON_MENU = True
DISPLAY_LINKS_ON_FOOTER = False
DISPLAY_MENUITEMS_ON_MENU = True
