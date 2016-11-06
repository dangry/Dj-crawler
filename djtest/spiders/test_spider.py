import scrapy

class TestSpider(scrapy.Spider):
    name = "test"
    allowed_domains = ["ww.1001tracklists.com"]
    start_urls = [
        "http://www.1001tracklists.com/tracklist/53459_martin-garrix-at-pepsi-mainstage-summerfestival-antwerp-belgium-2014-06-28.html"
    ]

    def parse(self, response):
      for item in response.xpath('.//*[@itemscope]'):
        print "Item:", item.xpath('@itemtype').extract()
        for property in item.xpath(
                """set:difference(.//*[@itemprop],
                                  .//*[@itemscope]//*[@itemprop])"""):
            print "Property:", property.xpath('@itemprop').extract(),
            print property.xpath('string(.)').extract()
            for position, attribute in enumerate(property.xpath('@*'), start=1):
                print "attribute: name=%s; value=%s" % (
                    property.xpath('name(@*[%d])' % position).extract(),
                    attribute.extract())
            print
        print

      #The above code retrieves the songs and music playlist

      for sel in response.xpath('//span[contains(@title, "played together with")]'):
            print sel.extract()

      #The above code takes out the songs tagged with a W (Played together with)