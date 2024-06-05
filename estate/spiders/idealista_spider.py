import scrapy
import urllib.parse

class IdealistaSpiderSpider(scrapy.Spider):
    name = "ideal"
    allowed_domains = ["www.idealista.com"]
    
    def start_requests(self):
        # username = 'customer-shahh_SpEr4-cc-es-city-madrid'
        # password = 'Shah130792024'
        # proxy_host = 'pr.oxylabs.io'
        # proxy_port = '7777'

        # URL encode the username and password
        # proxy_auth = f'{urllib.parse.quote(username)}:{urllib.parse.quote(password)}'

        proxy = f"https://customer-shahh_SpEr4:Shah130792024@us-pr.oxylabs.io:10000"

        yield scrapy.Request(
            url="https://www.idealista.com/en/venta-viviendas/madrigal-de-la-vera-caceres/",
            callback=self.parse,
            meta={
                    'proxy': proxy
                },

        )
    def parse(self, response):

        search_results = response.get("//section/article//div[@class='item-info-container ']")
        for each_result in search_results:
            detail_page_url = each_result.get(".//a").get()

        yield {
            "response_code":response.status,
            # "each_result": detail_page_url
        }


        
            
