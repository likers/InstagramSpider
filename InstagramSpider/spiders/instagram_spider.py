import scrapy
import json
import re
from InstagramSpider.items import InstagramspiderItem
from lxml import etree

class InstagramSpider(scrapy.Spider):
	