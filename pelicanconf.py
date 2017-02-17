#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Daniel Himmelstein'
SITENAME = "Satoshi Village"

DELETE_OUTPUT_DIRECTORY = True

PATH = 'content'
ARTICLE_PATHS = ['posts']
STATIC_PATHS = ['posts', 'favicon.ico', 'CNAME', '404.md']
EXTRA_PATH_METADATA = {'CNAME': {'path': 'CNAME'},
                       '404.md': {'path': '404.md'},}

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# URL settings
SITEURL = 'http://blog.dhimmel.com'
# Only enable document-relative URLs when developing
RELATIVE_URLS = False
ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'

USE_FOLDER_AS_CATEGORY = False

SUMMARY_MAX_LENGTH = 75

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('<b>Satoshi Village Blog</b>', '/'),
         ('&ndash; archives', '/archives'),
         ('<b>Daniel Himmelstein</b>', 'http://dhimmel.com/'),
         ('&ndash; about', 'http://dhimmel.com/about'),
         ('&ndash; research', 'http://dhimmel.com/research'),
         )

DEFAULT_PAGINATION = 10

# Pelicanyan
THEME = 'themes/pelicanyan/'
TWITTER_ACCOUNT = 'dhimmel'
DIRECT_TEMPLATES = ('index', 'archives', 'sitemap', 'robots', 'humans')
ROBOTS_SAVE_AS = 'robots.txt'
HUMANS_SAVE_AS = 'humans.txt'
SITEMAP_SAVE_AS = 'sitemap.xml'
DATE_FORMATS = {'en': '%B %d, %Y'}
SITEDESCRIPTION = "the blog of Daniel Himmelstein"
TYPOGRIFY = True
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.toc': {},
        'markdown.extensions.tables': {},
    },
    'output_format': 'html5',
}

# Services
DISQUS_SITENAME = 'satoshivillage'
#GOOGLE_ANALYTICS = 'UA-52757861-4'
#GA_ACCOUNT = 'UA-52757861-4' # used for pelicanyan

PIWIK_URL = 'piwik.dhimmel.com'
PIWIK_SITE_ID = 5
