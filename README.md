pitchfork-scrapy
================

Scraper goes to http://pitchfork.com/reviews/best/albums/ and follows next page link after collecting artist, album, date, score, and album artwork

spider is at pitchfork/spiders/best_new_albums_spider.py

Install scrapy, and run by: scrapy crawl best-new-albums -o scraped_data.json -t json
