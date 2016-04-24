import scrapy

class googleAppItem(scrapy.Item):
  
    
    url = scrapy.Field()
    app_name = scrapy.Field()
    description  = scrapy.Field()
    Num_star = scrapy.Field()
    what_is_new = scrapy.Field()
    subcategory = scrapy.Field()
    DatePublished = scrapy.Field()
    NumInstall = scrapy.Field()
    topDeveloper = scrapy.Field()
    size = scrapy.Field()
    softwareVersion = scrapy.Field()
    operatingSys = scrapy.Field()
    reviews_num = scrapy.Field()
    
    pass
