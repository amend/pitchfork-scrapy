# -*- coding: utf-8 -*-

# Scrapy settings for pitchfork project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'pitchfork'

SPIDER_MODULES = ['pitchfork.spiders']
NEWSPIDER_MODULE = 'pitchfork.spiders'
ITEM_PIPELINES = ['scrapy.contrib.pipeline.images.ImagesPipeline']
IMAGES_STORE= '/Users/andonimendoza/Development/scrape/pitchfork-scrapy/album-artwork'

DOWNLOAD_DELAY = .5    # delay in ms


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'pitchfork (+http://www.yourdomain.com)'
