import time

import requests
from lxml import etree


class doubanTop250:
    def __init__(self):
        pass

    def getHTMLText(self, url, code='UTF-8'):
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'
            }
            r = requests.get(url, headers=headers, timeout=30)
            r.raise_for_status()
            r.encoding = code
            return r.text
        except:
            return 'exception'

    def parseContent(self, html_str):
        # transfer html_str to HTML object
        selector = etree.HTML(html_str)

        # get li element lists
        li = selector.xpath('//ol[@class="grid_view"]/li')

        for li_item in li:
            # get the rank
            rank = li_item.xpath('div[@class="item"]/div[@class="pic"]/em/text()')
            print(rank[0])

            # get the title
            title = li_item.xpath('div[@class="item"]/div[@class="info"]//span[@class="title"]/text()')
            print(title[0])

            # get the link
            link = li_item.xpath('div[@class="item"]/div[@class="info"]/div[@class="hd"]/a//@href')
            print(link[0].strip())

            # get the director
            directorAndYear = li_item.xpath('div[@class="item"]/div[@class="info"]/div[@class="bd"]/p/text()')
            print(directorAndYear[0].strip())
            print(directorAndYear[1].strip())

            print('--------------------------split line-------------------------------------')
        time.sleep(1)

    def spider(self, index):
        ''' 豆瓣top250 '''
        URL = 'https://movie.douban.com/top250?start={0}&filter='.format(index)
        # get the html_str for dangdang.com
        html_str = self.getHTMLText(URL)
        self.parseContent(html_str)

    def process(self):
        for i in range(0, 10):
            self.spider(25 * i)


if __name__ == '__main__':
    doubanTop250 = doubanTop250()
    doubanTop250.process()
