import sys
from pathlib import Path

# Add current directory to Python path
current_dir = Path(__file__).parent
if str(current_dir) not in sys.path:
    sys.path.insert(0, str(current_dir))

from pelicanconf import *  # noqa: F403, E402
from pelicanconf import SITEURL  # noqa: E402

RELATIVE_URLS = False
DELETE_OUTPUT_DIRECTORY = True

# Enable feeds for production
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = "feeds/all.atom.xml"
FEED_ALL_RSS = "feeds/all.rss.xml"
