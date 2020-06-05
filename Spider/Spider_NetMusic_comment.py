import os

from selenium import webdriver


#
# def getHTMLText(session, url, code='UTF-8'):
#     try:
#         headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'
#         }
#         response = session.get(url, headers=headers, timeout=30)
#         response.raise_for_status()
#         response.encoding = code
#         return response.text
#     except:
#         return 'exception'
#
#
# def spider():
#     ''' 爬取网易云评论 '''
#     URL = 'https://music.163.com/song?id=29814898'
#
#     # get the html_str for zhonggong_mianshi
#     session = requests.session()
#     html_str = getHTMLText(session, URL)
#
#     # print(html_str)
#
#     # transfer html_str to HTML object
#     selector = etree.HTML(html_str)
#
#     # get data-tid
#     data_tid = selector.xpath('//div[@id="comment-box"]/@data-tid')
#     print(data_tid[0])
#
#     # get comment
#     parseComment(session, data_tid[0])
#
#
# def parseComment(session, data_tid):
#     comment_api = 'https://music.163.com/weapi/v1/resource/comments/{0}?csrf_token='.format(data_tid)
#     datas = {
#         'params': 'Xj9D5IoQJbhlMb2qhKoZ+6ReY53vYzQL0iflHnEkmJM0ur0F/hQ0ysRjOxupt3fHD9gVQnA+hADElIv7JXIT/6pd2QcekGQ8T2Nq6UrKahFb0CHoucvdCBfuXgPnC3Tv2f0VfLMsjHfnLDMzSklRg3atcqe9vQQxiSeY5Hk5NTfJDxqYuvaBnoP967G+vKD3',
#         'encSecKey': 'd66eaed5742b90362f8794a51a806553198f6bcdce9720f175e2072a0ecfc178563335866d17ab53533cb6e9e9c6148dd3fae023a4eaa42723e34f7192d8062a86d0fd758b64d6e15bb265425d53c22f46a163e18d0c3824e55cd3077f0d062402d1a5dc97dda44e5ff4710ce351310198c107234226d03c28e56bd5890639e1'
#     }
#     json = session.post(comment_api, data=datas)
#     print(json.text)

class NetMusicComment:
    def __init__(self):
        pass

    def spider(self, keyword):
        chromeDriver = os.getcwd() + '/chromedriver.exe'
        browser = webdriver.Chrome(chromeDriver)
        URL = 'https://music.163.com/#/search/m/?s={0}'.format(keyword)
        print(URL)
        browser.get(URL)
        print(browser.page_source)
        browser.close()


if __name__ == '__main__':
    netMusicComment = NetMusicComment()
    netMusicComment.spider('可惜没如果')
