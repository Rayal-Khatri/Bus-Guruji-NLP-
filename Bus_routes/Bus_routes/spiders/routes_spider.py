import scrapy


class RoutesSpiderSpider(scrapy.Spider):
    name = "routes_spider"
    allowed_domains = ["nepal-streets.openalfa.com"]
    start_urls = ["https://nepal-streets.openalfa.com/lalitpur/bus-routes"]

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse)

    def parse(self, response):
        routes = response.css('label a::attr(href)').getall()
        for route in routes:
            full_url = response.urljoin(route)
            print('***********************',full_url)
            yield scrapy.Request( url = full_url, callback=self.parse_bus_stops)
        pass

    def parse_bus_stops(self, response):
        title = response.css('.title h1::text').get()
        stops = response.css('li::text').getall()
        yield {
            'title': title,
            'stops': stops
        }