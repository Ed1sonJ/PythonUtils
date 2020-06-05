import requests
from lxml import etree


class jd:
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
        li = selector.xpath('//div[@id="J_goodsList"]/ul/li')

        for li_item in li:
            div_item = li_item.xpath('div[@class="gl-i-wrap"]')[0]

            # get the title
            title = div_item.xpath('div[@class="p-name p-name-type-2"]/a/@title')
            print(title[0])

            # get the price
            price = div_item.xpath('div[@class="p-price"]//i/text()')
            print(price[0].replace('¥', ''))

            # get the store
            publish_house = div_item.xpath('div[@class="p-shop"]//a/@title')
            print(publish_house[0])

            # get the buy link
            buy_link = div_item.xpath('div[@class="p-name p-name-type-2"]/a/@href')
            print(buy_link[0])

            print('--------------------------split line-------------------------------------')

    def spider(self, keyword):
        ''' 爬取京东网 '''
        URL = 'https://search.jd.com/Search?keyword={0}&enc=utf-8&wq={0}'.format(keyword)

        # get the html_str for dangdang.com
        html_str = self.getHTMLText(URL)
        self.parseContent(html_str)


if __name__ == '__main__':
    jd = jd()
    jd.spider('纸巾')
