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
            soup = BeautifulSoup(response.text, 'html.parser')
            return soup
        except requests.HTTPError as e:
            if hasattr(e, 'reason'):
                print('连接失败,错误原因', e.reason)
                return None

    #获取title
    def gettitle(self):
        soup = self.getsoup()
        titledata = soup.select('meta[name="citation_title"]')
        title = titledata[0]['content']
        print(titledata[0]['content'])
        return title

    #获取下载链接
    def geturl(self):
        soup = self.getsoup()
        urlpagedata = soup.select('meta[name="citation_pdf_url"]')
        urlpage = urlpagedata[0]['content']
        print(urlpagedata[0]['content'])
        return urlpage

    #下载pdf到本地
    def downloadpdf(self):
        title = self.gettitle()
        urlpage = self.geturl()
        responsepage = requests.get(urlpage)
        pdfname = str(title) + '.pdf'
        with open(pdfname, 'wb') as f:
            f.write(responsepage.content)


def main():
    paper = papercrawler('http://arxiv.org/abs/1608.07531')
    paper.downloadpdf()


if __name__ == '__main__':
    main()
