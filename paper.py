# -*- coding:utf-8 -*-
__author__ = 'huposeya'
#单页文章的下载，以标题.pdf的形式保存

import requests
from bs4 import BeautifulSoup

class papercrawler:
    def __init__(self, url):
        self.url = url

    #获取网页源码
    def getsoup(self):
        try:
            response = requests.get(self.url)
        except requests.HTTPError as e:
            if hasattr(e, 'reason'):
                print('连接失败,错误原因', e.reason)
            else:
                print('连接失败, 未知原因')
            return None

        self.soup = BeautifulSoup(response.text, 'html.parser')
        return self.soup

    #获取title
    def gettitle(self):
        soup = self.soup
        titledata = soup.select('meta[name="citation_title"]')
        title = titledata[0]['content']
        print('title: %s' % titledata[0]['content'])
        return title

    #获取下载链接
    def geturl(self):
        soup = self.soup
        urlpagedata = soup.select('meta[name="citation_pdf_url"]')
        urlpage = urlpagedata[0]['content']
        print(urlpagedata[0]['content'])
        return urlpage

    #下载pdf到本地
    def downloadpdf(self):
        self.getsoup()
        title = self.gettitle()
        urlpage = self.geturl()
        responsepage = requests.get(urlpage)
        pdfname = str(title) + '.pdf'
        with open(pdfname, 'wb') as f:
            f.write(responsepage.content)


def main(url):
    paper = papercrawler(url)
    paper.downloadpdf()


if __name__ == '__main__':
    url = 'http://arxiv.org/abs/1608.07531'
    main(url)
