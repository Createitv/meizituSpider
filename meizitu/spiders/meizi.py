import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from meizitu.items import MeizituItem


class MeiziSpider(CrawlSpider):
    name = 'meizi'
    # allowed_domains = ['meizitu']
    start_urls = ['http://www.mzitu.com']

    rules = (
        Rule(LinkExtractor(allow=r'/page/.*?'),
             callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = MeizituItem()
        infos = response.css("#pins li")
        for info in infos:
            page = response.css(".current::text").get()
            href = info.xpath("./a/img/@data-original").get()
            name = info.xpath("./a/img/@alt").get()
            item = {
                'href': href,
                'name': name,
                'page': page
            }
            yield item
