#网络爬虫学习

from bs4 import BeautifulSoup as bf
from urllib.request import urlopen

html = urlopen("http://www.baidu.com/")
obj = bf(html.read(), 'html.parser')
clip = obj.head.title
print(clip)
