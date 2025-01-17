ARCHIVES_SAVE_AS = "archives/index.html"
ARCHIVES_URL = "archives/"
AUTHOR = "julz"
AUTHORS_SAVE_AS = "authors/index.html"
AUTHORS_URL = "authors/"
CATEGORIES_SAVE_AS = "categories/index.html"
CATEGORIES_URL = "categories/"
DEFAULT_CATEGORY = "Tech"
DEFAULT_LANG = "en"
DEFAULT_PAGINATION = 10
DELETE_OUTPUT_DIRECTORY = True
DISPLAY_CATEGORIES_ON_MENU = True
GITHUB_URL = "https://github.com/julzhk"
HOME_COVER = 'https://geekyshacklebolt.github.io/blog/images/my-blog-header-bg.jpg'
OUTPUT_SOURCES = True
PATH = "content"
RELATIVE_URLS = True
SITENAME = "Another GitHub Blog!"
SITEURL = ""
FEED_DOMAIN = SITEURL
TAGS_SAVE_AS = "tags/index.html"
TAGS_URL = "tags/"
THEME = "attila"
THEME_TEMPLATES_OVERRIDES = ["attila"]
TIMEZONE = "Canada/Atlantic"
TYPOGRIFY = True
TYPOGRIFY_DASHES = "oldschool"

# Make the URLs of article permalink pages nicer.
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SOURCE_URL = "{article.url}index{OUTPUT_SOURCES_EXTENSION}"

# Make the URLs of period archive pages nicer.
YEAR_ARCHIVE_SAVE_AS = "{date:%Y}/index.html"
YEAR_ARCHIVE_URL = "{date:%Y}/"
MONTH_ARCHIVE_SAVE_AS = "{date:%Y}/{date:%m}/index.html"
MONTH_ARCHIVE_URL = "{date:%Y}/{date:%m}/"
DAY_ARCHIVE_SAVE_AS = "{date:%Y}/{date:%m}/{date:%d}/index.html"
DAY_ARCHIVE_URL = "{date:%Y}/{date:%m}/{date:%d}/"

# Make the URLs of static pages nicer.
PAGE_SAVE_AS = '{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SOURCE_URL = "{page.url}index{OUTPUT_SOURCES_EXTENSION}"

LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Oatcake", "https://github.com/seanh/oatcake"),
    ("GitHub", "https://github.com/seanh/sidecar"),
)

SOCIAL = [
    ("Mastodon", "https://mastodon.social/@seanh"),
    ("Pinboard", "https://pinboard.in/u:seanh"),
]

SIDECAR_MENU = [
    "HOME",
    "MENUITEMS",
    "PAGES",
    "TAGS",
    "ARCHIVES",
]

SIDECAR_TAGLINE = [
    "TIME",
    "AUTHORS",
    "TAGS",
]
