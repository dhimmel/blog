# Python 3 pelican configuration file for blog.dhimmel.com
# https://docs.getpelican.com/en/stable/settings.html

AUTHOR = "Daniel Himmelstein"
SITENAME = "Satoshi Village"

DELETE_OUTPUT_DIRECTORY = False

PATH = "content"
ARTICLE_PATHS = ["posts"]
STATIC_PATHS = ["favicon.ico"]
EXTRA_PATH_METADATA = dict()

# Static files to copy from content to output
for name in "CNAME", "404.md", ".nojekyll":
    STATIC_PATHS.append(name)
    EXTRA_PATH_METADATA[name] = {"path": name}

TIMEZONE = "America/New_York"

DEFAULT_LANG = "en"

# URL settings
SITEURL = "https://blog.dhimmel.com"
# document-relative URLs for developing
RELATIVE_URLS = True
ARTICLE_URL = "{slug}/"
ARTICLE_SAVE_AS = "{slug}/index.html"

USE_FOLDER_AS_CATEGORY = False

SUMMARY_MAX_LENGTH = 75

# Feed generation is usually not desired when developing
FEED_DOMAIN = None
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = [
    ("<b>Satoshi Village Blog</b>", "/"),
    ("&ndash; archives", "/archives"),
    ("<b>Daniel Himmelstein</b>", "https://dhimmel.com/"),
    ("&ndash; about", "https://dhimmel.com/about"),
    # ("&ndash; research", "https://dhimmel.com/research"),
]

DEFAULT_PAGINATION = 10

# Pelicanyan
THEME = "themes/pelicanyan/"
TWITTER_ACCOUNT = "dhimmel"
DIRECT_TEMPLATES = ("index", "archives", "sitemap", "robots", "humans")
ROBOTS_SAVE_AS = "robots.txt"
HUMANS_SAVE_AS = "humans.txt"
SITEMAP_SAVE_AS = "sitemap.xml"
DEFAULT_DATE_FORMAT = "%Y-%m-%d"
SITEDESCRIPTION = "the blog of Daniel Himmelstein"
TYPOGRIFY = True
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.toc": {},
        "markdown.extensions.tables": {},
    },
    "output_format": "html5",
}

# External services
DISQUS_SITENAME = "satoshivillage"

# GOOGLE_ANALYTICS = 'UA-52757861-4'
# GA_ACCOUNT = 'UA-52757861-4' # used for pelicanyan

PIWIK_URL = "piwik.dhimmel.com"
PIWIK_SITE_ID = 5
