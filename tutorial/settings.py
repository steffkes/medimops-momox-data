# Scrapy settings for tutorial project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
ISBNS = [
    "9783423209694",
    "9783527507993",
    "9783593398532",
    "9783958751750",
    "9781101886724",
    "9783734104091",
    "9783947188857",
    "9783446414396",
    "9783548289199",
    "9783548289212",
    "9783548289229",
    "9781101886694",
    "9781101904220",
    "9783548060224",
    "9781409168744",
    "9781409168799",
    "9783423209694",
    "9783499256356",
    "9783551551672",
    "9783551551696",
    "9783551551689",
    "9780345816023",
    "9781449474256",
    "9781524763138",
    "9781408711392",
    "9780099590088",
    "9781439199190",
]

BOT_NAME = "tutorial"

SPIDER_MODULES = ["tutorial.spiders"]
NEWSPIDER_MODULE = "tutorial.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "momox-medimops-crawler (+momox-mediamops-crawer@mail.gelungen.es)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
TELNETCONSOLE_ENABLED = False

REDIRECT_ENABLED = True

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
    "scrapy.spidermiddlewares.httperror.HttpErrorMiddleware": None,
    "scrapy.spidermiddlewares.offsite.OffsiteMiddleware": None,
    "scrapy.spidermiddlewares.referer.RefererMiddleware": None,
    "scrapy.spidermiddlewares.urllength.UrlLengthMiddleware": None,
    "scrapy.spidermiddlewares.depth.DepthMiddleware": None
    #    'tutorial.middlewares.TutorialSpiderMiddleware': 543,
}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    "scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware": None,
    "scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware": None,
    "scrapy.downloadermiddlewares.useragent.UserAgentMiddleware": None,
    "scrapy.downloadermiddlewares.retry.RetryMiddleware": None,
    "scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware": None,
    "scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware": None,
    "scrapy.downloadermiddlewares.redirect.RedirectMiddleware": 100,
    "scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware": None,
    #    'tutorial.middlewares.TutorialDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'tutorial.pipelines.TutorialPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
