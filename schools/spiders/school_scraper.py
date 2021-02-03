# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import json
from schools.items import SchoolsItem
from scrapy.loader import ItemLoader

class SchoolScraperSpider(scrapy.Spider):
    name = 'school_scraper'
    allowed_domains = ['ntschools.net']

    headers = {

        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        "Referer": "https://directory.ntschools.net/",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
        "X-Requested-With": "Fetch"
    }

    def start_requests(self):
        url = 'https://directory.ntschools.net/api/System/GetAllSchools'
        yield Request(url, callback=self.parse_api, headers=self.headers)

    def parse_api(self, response):
        base_url = 'https://directory.ntschools.net/api/System/GetSchool?itSchoolCode='
        raw_data = response.body
        data = json.loads(raw_data)
        for school in data:
            school_code = school['itSchoolCode']
            school_url = base_url + school_code
            request = Request(school_url, callback=self.parse_school, headers=self.headers)
            yield request

    def parse_school(self, response):

        l = ItemLoader(item=SchoolsItem(), response=response)
        raw_data = response.body
        data = json.loads(raw_data)

        
        l.add_value('name', data['name'])
        l.add_value('phone_number', data['telephoneNumber'])
        l.add_value('email', data['mail'])
        l.add_value('physical_address', data['physicalAddress']['displayAddress'])
        l.add_value('postal_address', data['postalAddress']['displayAddress'])

        return l.load_item()
        
        """

        yield {
            'name': data['name'],
            'phone_number': data['telephoneNumber']
        }

        """