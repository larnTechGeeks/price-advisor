import scrapy

class PricesSpider(scrapy.Spider):
    name = 'prices'
    allowed_domains = ['jumia.co.ke']
    search_url = 'https://www.jumia.co.ke/'
    start_urls = [search_url]

    def __init__ (self, search_term="", **kwargs):
        self.search_term = search_term
        self.jumia_url = "https://www.jumia.co.ke/"
        self.start_urls = [self.jumia_url]
        super().__init__(**kwargs)

    def parse(self, response):
        link_ = f"{self.start_urls[0]}catalog/?q={self.search_term}"
        yield response.follow(link_, callback=self.parse_product_search)

    def parse_product_search(self, response):
        all_category_products_found = response.css('article.prd._fb.col.c-prd')
        print("All Procusts ", all_category_products_found)
        for product in all_category_products_found:
            yield {
                "product_name": product.css('h3.name::text').get(),
                "discounted_price": product.css('div.prc::text').get(),
                "price": product.css('div.old::text').get(),
                "ratings": product.css('div.stars._s::text').get(),
                "is_shipped": product.css('div.bdg._glb._xs').get()
            } 
