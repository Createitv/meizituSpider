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
            detail_url = info.css("a::attr(href)").get()
            page = response.css(".current::text").get()
            name = info.xpath("./a/img/@alt").get()
            item = {
                'name': name,
                'page': page
            }
            yield scrapy.Request(url=detail_url, callback=self.parse_detail, meta={'item': item}, dont_filter=True)



    def parse_detail(self, response):
        item = response.meta.get('item')
        img_url = response.xpath('//img[@class="blur"]/@src').get()
        img_name = img_url.split('/')[-1]
        next_page_flag = response.xpath(
            '//div[@class="pagenavi"]/a[last()]/span/text()').get()
        item['img_url'] = img_url
        item['img_name'] = img_name
        yield item
        if next_page_flag == "下一页»":
            next_page = response.xpath(
                '//div[@class="pagenavi"]//a[last()]/@href').get()
            yield scrapy.Request(url=next_page, callback=self.parse_detail, meta={'item': item})
        else:
            print(f"{item['page']}页{item['img_name']}爬取结束")
# 下一页»
