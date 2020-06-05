import requests
from lxml import etree


class zhonggong_mianshi:
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
        li = selector.xpath('//div[@class="lh_Hotrecommend"]/ul/li')

        for li_item in li:
            # get the date
            date = li_item.xpath('span/font/text()')
            if (len(date) == 0):
                date = li_item.xpath('span/text()')
            print(date[0])

            # get the link
            link = li_item.xpath('a')[1].xpath('@href')
            # print(link[0])

            # parse each page
            self.parseEachPage(link[0])

            print('--------------------------split line-------------------------------------')

    def parseEachPage(self, link):
        html_str = self.getHTMLText(link, 'gb2312')
        # transfer html_str to HTML object
        selector = etree.HTML(html_str)

        # get li element lists
        p_list = selector.xpath('//div[@class="offcn_shocont"]/p')

        index = 0
        for p in p_list:
            index += 1
            if index >= 4:
                if p.text is None:
                    p_strong_text = p.xpath('strong/text()')
                    if len(p_strong_text) != 0:
                        print(p_strong_text[0])
                else:
                    print(p.text)

    def spider(self):
        URL = URL = 'http://www.offcn.com/mianshi/mryl/'
        html_str = self.getHTMLText(URL, 'gb2312')
        self.parseContent(html_str)


if __name__ == '__main__':
    zhonggong_mianshi = zhonggong_mianshi()
    zhonggong_mianshi.spider()
