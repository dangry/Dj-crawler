import scrapy


class DjtestTracklist(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    tracklistName = scrapy.Field()
    tracklist = scrapy.Field()
    tracklistGenres = scrapy.Field()
    tracklistAuthor = scrapy.Field()
    tracklistDatePublished = scrapy.Field()
    tracklistNumTracks = scrapy.Field()
    pass

