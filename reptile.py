#网络爬虫学习

from bs4 import BeautifulSoup as bf
from urllib.request import urlopen, urlretrieve
'''
html = urlopen("http://www.baidu.com/")
obj = bf(html.read(), 'html.parser')
#获取百度首页标题
clip = obj.head.title
#pic_info = obj.find_all('img')
pic_info = obj.find_all('img', class_="index-logo-src")
for i in range(0, 1):
    print(pic_info[i]['hidefocus'])
#pic_url = "https:" + pic_info[0]['src']
#urlretrieve(pic_url, "./pics/baidu.png")
'''

#高亮文字显示
hilight = '\033[1;37;43m'
#默认文字显示
dcolor = '\033[0m'

"""
#xpath学习
from lxml import etree
html_text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-2 item-3"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''

#etree能校正html_text的格式
#html文本格式
html = etree.HTML(html_text)
html_pname = "./htmls/test.html"
with open(html_pname, "w+") as zf:
    #转换成bytes字符串并解码
    zf.write(etree.tostring(html).decode('utf-8'))
zhtml = etree.parse(html_pname, etree.HTMLParser())
zdict = dict()
#/ 直接子节点，// 子孙节点，. 当前节点，.. 父节点，@ 选取属性 contains(属性， 属性值) 匹配包含该属性值 [序号] 第几号节点
#属性匹配：[属性名=属性值], 获取属性：@属性名
zdict['搜索所有子节点及子孙节点'] = zhtml.xpath('//*')
zdict['搜索所有名称为a的节点'] = zhtml.xpath('//a')
zdict['搜索所有名称为li的直接子节点下的所有名称为a的节点'] = zhtml.xpath('//ul//a')
zdict['搜索href属性为link4.html的a节点的父节点的class属性'] = zhtml.xpath('//a[@href="link4.html"]/../@class')
zdict['搜索所有li节点下class属性为item-0的所有节点'] = zhtml.xpath('//li[@class="item-0"]')
zdict['搜索所有li节点属性为item-0的直接子节点后的文本'] = zhtml.xpath('//li[@class="item-0"]/text()')
zdict['搜索所有li节点下属性为item-0的a节点的文本'] = zhtml.xpath('//li[@class="item-1"]/a/text()')
zdict['搜索所有li节点属性为item-0的所有节点后的文本'] = zhtml.xpath('//li[@class="item-0"]//text()')
zdict['搜索所有li节点下a节点的href属性'] = zhtml.xpath('//li/a/@href')
zdict['搜索所有li节点下包含class属性为item-3的a的节点的文本'] = zhtml.xpath('//li[contains(@class, "item-3")]/a/text()')
zdict['搜索第三号li节点的a节点的文本'] = zhtml.xpath('//li[3]/a/text()')
for zd in zdict:
    print(hilight + zd + dcolor, ':\n', zdict[zd])
"""

#'''
#Mozilla/5.0 (Windows NT 10.0; WOW64)
from lxml import etree
import requests as re
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)'}
zstr = re.get('https://www.zhihu.com/question/352470379', headers=headers)
zt = etree.HTML(zstr.text)

mdict = dict()
mdict['问题'] = zt.xpath('//*[@class="QuestionHeader-title"]/text()')
mdict['问题描述'] = zt.xpath('//*[contains(@class, "QuestionRichText")]//span/text()')
mdict['问题回复'] = zt.xpath('//*[contains(@class, "RichText ztext")]//p/text()')
mdict['问题关注数'] = str(zt.xpath('//*[@class="NumberBoard-itemValue"]/text()')[0])
mdict['问题浏览数'] = str(zt.xpath('//*[@class="NumberBoard-itemValue"]/text()')[1])

#'x'.join(y) 当y为元祖或者列表(字符串也能)时，能以x为间隔符号分割元素并去除引号和中括号输出
for key, value in mdict.items():
    print(hilight + key + dcolor)
    if(type(value) == type(str())):
        print(value)
    else:
        print("\n************\n".join(value))
#'''

