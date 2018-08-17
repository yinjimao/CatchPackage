# coding=utf-8

from urllib import request
from urllib import response
import re


def getHtml(urlpath):
    rs = request.urlopen(urlpath)
    html = rs.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    html = html.decode('utf-8')  # python3
    imglist = re.findall(imgre, html)
    x = 1
    for img in imglist:
        request.urlretrieve(img, '%s.jpg' %x)
        x += 1
    return imglist

path = "http://tieba.baidu.com/p/4040087257/"
html=getHtml(path)
print(html)
getImg(html)