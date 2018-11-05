# -*-coding:utf-8 -*-
import os
import time
import sys
import importlib
importlib.reload(sys)
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
file_name = 'movies_top250.csv'
file_content = ''
file_content +=  "电影名\t"+"评分\t"+'评价人次\t'+'短评\t'+'\n'
target_dir = os.getcwd() + '/douban/'
#alllink=set()
def movies_spider(start):
    #internalLink=[]
    #global alllink
    global file_content
    url = "https://movie.douban.com/top250?start=%d" % start
    html =urlopen(url)
    bsObj= BeautifulSoup(html)
    movie_list =bsObj.find_all('div', {'class': 'item'})
    for item in movie_list:
        info = item.find('div', {'class': 'info'})
       # link = info.find('a',href=re.compile("^(https://movie.douban.com/subject/)"))
        #links=link.attrs['href']
        name = info.find('span', {'class': 'title'}).string
        #电影名称
        #bd   = info.find('div',{'class':"bd"})#电影导演
        #bds=bd.find('p',{'class':''}).string
        rating_num = info.find('span', {'class': 'rating_num'}).string
       #评分
        total = info.find('span', {'class': 'rating_num'}).find_next_sibling().find_next_sibling().string
       #多少人评价
        inq = info.find('span', {'class': 'inq'})
       #短评
        #html2=urlopen(links)
        #bsObj2=BeautifulSoup(html2)
        #for finditem in
        try:
            quote = inq.get_text()
        except AttributeError:
            quote = 'None'
            print("Type error")
        #html2=urlopen(links)
        #bsObj2=BeautifulSoup(html2)
        #local_movie_list=bsObj2.findAll('div', {'class': 'info'})
        #for items in local_movie_list:
         #   #电影导演
         #   daoyan= items.find('span',{'class':'name'})

        file_content += "%s\t%s\t%s\t%s\t\n" % (  name, rating_num, total, quote)
def do_spider():
    for start in (range(250)[::25]):
        movies_spider(start)

def get_dir():
    path = os.path.join(os.getcwd(), "doubanTop250")
    if os.path.exists(path):
        return path
    os.mkdir(path)
    return path


if __name__ == '__main__':
    do_spider()
    with open(get_dir() + '/' + file_name, 'w') as f:
        f.write(file_content)

    print("DONE")