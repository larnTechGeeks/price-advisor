import sys
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from priceadvisor.spiders.prices import PricesSpider
 
 
process = CrawlerProcess(get_project_settings())
#crawler = PricesSpider
process.crawl(PricesSpider, search_term=sys.argv[1:])
process.start()