#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Daniel Himmelstein'
SITENAME = "Satoshi Village"
SITEURL = 'http://blog.dhimmel.com'
DELETE_OUTPUT_DIRECTORY = True

PATH = 'content'
ARTICLE_PATHS = ['posts']
STATIC_PATHS = ['posts', 'favicon.ico', 'CNAME']
EXTRA_PATH_METADATA = {'CNAME': {'path': 'CNAME'},}

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# URL settings
ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'

USE_FOLDER_AS_CATEGORY = False

SUMMARY_MAX_LENGTH = 75

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Archives', '/archives'),
         ('Home', 'http://dhimmel.com/'),
         ('About', 'http://dhimmel.com/about'),
         ('Research', 'http://dhimmel.com/research'),
         ('Blog', '/'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Pelicanyan
THEME = 'themes/pelicanyan/'
TWITTER_ACCOUNT = 'dhimmel'
DIRECT_TEMPLATES = ('index', 'archives', 'sitemap', 'robots', 'humans')
ROBOTS_SAVE_AS = 'robots.txt'
HUMANS_SAVE_AS = 'humans.txt'
SITEMAP_SAVE_AS = 'sitemap.xml'
DATE_FORMATS = { 'en': '%B %d, %Y', }
SITEDESCRIPTION = "the blog of Daniel Himmelstein"
TYPOGRIFY=True

# Services
DISQUS_SITENAME = 'satoshivillage'
GOOGLE_ANALYTICS = 'UA-52757861-4'
GA_ACCOUNT = 'UA-52757861-4'

