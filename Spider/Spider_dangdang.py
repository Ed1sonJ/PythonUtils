import requests
from lxml import etree


class dangdang():
    def __init__(self, keyword):
        self.keyword = keyword

    def getHTMLText(self, url, code='UTF-8'):
        try:
            r = requests.get(url, timeout=30)
            r.raise_for_status()
            r.encoding = code
            return r.text
        except:
            return 'exception'

    def parseContent(self, html_str):

        # transfer html_str to HTML object
        selector = etree.HTML(html_str)

        # get li element lists
        li = selector.xpath('//div[@id="search_nature_rg"]/ul/li')

        for li_item in li:
            # get the title
            title = li_item.xpath('a/@title')
            print(title[0])

            # get the price
            price = li_item.xpath('p[@class="price"]//span[@class="search_now_price"]/text()')
            print(price[0].replace('¥', ''))

            # get the publishing house
            publish_house = li_item.xpath('p[@class="search_book_author"]//a[@name="P_cbs"]/text()')
            print(publish_house[0])

            # get the buy link
            buy_link = li_item.xpath('p[@class="name"]/a/@href')
            print(buy_link[0])

            print('--------------------------split line-------------------------------------')

    def spider(self):
        ''' 爬取当当网 '''
        URL = 'http://search.dangdang.com/?key={0}'.format(self.keyword)

        # get the html_str for dangdang.com
        html_str = self.getHTMLText(URL, 'GB2312')

        self.parseContent(html_str)


if __name__ == '__main__':
    dangdang = dangdang('python')
    dangdang.spider()
