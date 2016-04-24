import scrapy
import re
from appcrawl.items import googleAppItem


class googleAppSpider(scrapy.Spider):
    name = "googleApp"
    allowed_domains = ['play.google.com']
    start_urls = ['https://play.google.com/store/apps/category/GAME/collection/topselling_new_free?authuser=0']

    def parse(self,response):
        for i in range(0,10): 
            yield scrapy.FormRequest(url="https://play.google.com/store/apps/category/GAME/collection/topselling_new_free?authuser=0", method="POST", formdata={'start':str(i*60),'num':'60','numChildren':'0','ipf':'1','xhr':'1','token':'m1VdlomIcpZYfkJT5dktVuqLw2k:1455483261011'}, callback=self.data_parse)

    def data_parse(self,response):
        item = googleAppItem()
        map = {}
        links = response.xpath("//a/@href").re(r'/store/apps/details.*')
        for l in links:
            if l not in map:
                map[l] = True
                l = "http://play.google.com"+str(l)
                request = scrapy.Request(l,callback=self.parse_every_app)
                item['url'] = l
                request.meta['item'] = item
                yield request


    def parse_every_app(self,response):
       

        for sel in response.xpath('//div[@itemscope="itemscope"]'):
            item = googleAppItem()
            item["app_name"] = response.xpath('//div[@class="id-app-title"]/text()').extract()
            item["description"] = response.xpath('//div[@itemprop="description"]//*/text()').extract()
            item['Num_star'] = response.xpath('//div[@class="score"]/text()').extract()
            item['subcategory']=response.xpath('//a[@class="document-subtitle category"]/span[@itemprop="genre"]/text()').extract()[-1]
            item['what_is_new'] = response.xpath('//div[@class="recent-change"]//*/text()').extract()
            item['DatePublished'] = response.xpath('//div[@itemprop="datePublished"]/text()').extract()
            item['NumInstall'] = response.xpath('//div[@itemprop="numDownloads"]/text()').extract()
            item['topDeveloper'] = response.xpath('//span[@class="badge-title"]/text()').extract()
            item['size'] = response.xpath('//div[@itemprop="fileSize"]/text()').extract()
            item['softwareVersion'] = response.xpath('//div[@itemprop="softwareVersion"]/text()').extract()
            item['operatingSys'] = response.xpath('//div[@itemprop="operatingSystems"]/text()').extract()
            item['reviews_num'] = response.xpath('//span[@class="reviews-num"]/text()').extract()
                                                 
            yield item
                                                