# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
class CustomImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        # 从items中获取要下载图片的url, 根据url构造Requeset()对象, 并返回该对象
        # sort_title = item['sort_title']
        try:
            image_url = item['href']
            yield Request(image_url, meta={'item': item})
        except:
            image_url = 'https://www.qisuu.la/modules/article/images/nocover.jpg'
        yield Request(image_url, meta={'item': item})

    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        return '{}/{}.jpg'.format(item['page'], item['name'])

    def item_completed(self, results, item, info):
        print(results)
        return item
