AUTHOR = 'Ameising'
SITENAME = 'Ameising'
SITEURL = ""

THEME = "ameising-site"

PATH = "content"

OUTPUT_PATH = 'docs/'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
INDEX_SAVE_AS = 'index.html'

PORT = 8080

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'no'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Log in", "https://ameising.ai/app"),
    ("Sign up", "https://ameising.ai/auth/register"),
)

# Social widget
SOCIAL = (
    ("LinkedIn", "#"),
    ("X (Twitter)", "#"),
)

STATIC_PATHS = [
    'images',
    'extra',
]

EXTRA_PATH_METADATA = {
    'extra/android-chrome-192x192.png': {'path': 'resources/android-chrome-192x192.png'},
    'extra/android-chrome-512x512.png': {'path': 'resources/android-chrome-512x512.png'},
    'extra/apple-touch-icon.png': {'path': 'resources/apple-touch-icon.png'},
    'extra/favicon-16x16.png': {'path': 'resources/favicon-16x16.png'},
    'extra/favicon-32x32.png': {'path': 'resources/favicon-32x32.png'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/site.webmanifest': {'path': 'site.webmanifest'},
    'extra/ameising.css': {'path': 'css/ameising.css'},
}

STYLESHEET_URL = '/css/ameising.css'

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
