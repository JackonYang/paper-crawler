# -*- coding:utf-8 -*-
__author__ = 'huposeya'
# 用于获取下载列表

import time
import requests
from bs4 import BeautifulSoup

import paper

def geturllist(urllist):
    responselist = requests.get(urllist)
    soup = BeautifulSoup(responselist.text, 'html.parser')
    urldata = soup.find_all('span', class_="list-identifier")
    list = []
    for i in urldata:

        url = 'http://arxiv.org/' + i('a')[0]['href']

        print 'downloading url: %s' % url
        paper_page = paper.papercrawler(url)
        paper_page.downloadpdf()

        print 'sleeping 5s...'
        time.sleep(5)

        list.append('http://arxiv.org/' + i('a')[0]['href'])
    return list


def main(url):
    geturllist(url)

if __name__ == '__main__':
    url = 'http://arxiv.org/list/cs/recent'
    main(url)
