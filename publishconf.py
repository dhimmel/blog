from pelicanconf import *  # noqa: F403
from pelicanconf import SITEURL

RELATIVE_URLS = False
DELETE_OUTPUT_DIRECTORY = True

# Enable feeds for production
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = "feeds/all.atom.xml"
FEED_ALL_RSS = "feeds/all.rss.xml"
