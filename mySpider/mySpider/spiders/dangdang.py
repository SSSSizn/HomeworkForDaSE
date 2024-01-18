import scrapy
import chardet
from mySpider.items import DANGDANG


class DangdangSpider(scrapy.Spider):
    name = "dangdang"
    allowed_domains = ["book.dangdang.com"]
    start_urls = [f'https://category.dangdang.com/pg{i}-cp01.54.00.00.00.00.html' for i in range(1, 10)]

    def parse(self, response):
        books = response.xpath('//ul[@class="bigimg"]//li')
        items = []

        for book in books:
            item = DANGDANG()
            title = book.xpath('.//p[@class="name"]/a/text()').get()
            short_title = book.xpath('.//a[@class="pic"]/@title').get()
            author = book.xpath(
                './/p[@class="search_book_author"]/span/a/text()').get()
            now_price = book.xpath(
                './/p[@class="price"]/span[@class="search_now_price"]/text()').get()
            pre_price = book.xpath(
                './/p[@class="price"]/span[@class="search_pre_price"]/text()').get()

            item['title'] = title
            item['author'] = author
            item['now_price'] = now_price
            item['short_title'] = short_title
            item['pre_price'] = pre_price
            items.append(item)
        return items
