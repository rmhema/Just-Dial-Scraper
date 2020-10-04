import scrapy


class JustdialSpiderSpider(scrapy.Spider):
    name = 'justdial_spider'
    start_urls = ['https://www.justdial.com/Delhi/Pure-Veg-Restaurants/nct-10396867']

    def parse(self, response):
        for quote in response.selector.xpath('//li[@class="cntanr"]'):
            yield {
                'Restaurant Name': quote.xpath('.//span[@class="lng_cont_name"]/text()').extract_first(),
                'Ratings': quote.xpath('.//span[@class="green-box"]/text()').extract_first(),
                'Address': quote.xpath('.//span[@class="cont_fl_addr"]/text()').extract_first(),
                'Contact Number': quote.xpath(
                    './/p[@class="contact-info "]/span/a/b/span/@class|.//p[@class="contact-info "]/span/a/span/@class').extract()

            }
        next_page = response.selector.xpath("//a[@rel='next']/@href").extract_first()
        if next_page is not None:
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link, callback=self.parse)
