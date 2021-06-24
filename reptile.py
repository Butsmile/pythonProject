#网络爬虫学习

def zinstall(zpack=None):
    with open("zinstall.bat", "w+") as zi:
        zi.write("@echo off\n")
        zi.write("D:\PyCharm_Projects\pythonProject\\venv\Scripts\python.exe -m pip install " + zpack + '\n')
        zi.write("pause")

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
zdict['搜索所有名称为li的直接子节点下的所有名称为a的节点'] = zhtml.xpath('//li//a')
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
import requests as req

def reptile_0():
    print('')
    url = 'https://item.jd.com/26809739632.html'
    try:
        r = req.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.text)
    except:
        print('爬取失败！')

#爬取colorhub网站首页的所有图片
def reptile_1():
    zheader = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3947.100 Safari/537.36'}
    url = "https://colorhub.me"
    zhtml = req.get(url, headers=zheader)
    #print(zhtml.text)
    zhtml.raise_for_status()
    phtml = etree.HTML(zhtml.text)
    #zdict = dict()
    img_title = phtml.xpath('//*[contains(@class, "card-img")]//@title')
    img_src = phtml.xpath('//*[contains(@class, "card-img")]//@src')
    print(img_title)
    print(img_src)
    zsize = len(img_title)
    print(zsize)
    for a in range(0, 4):
        print(a, end=' ')
    if False:
        for i in range(0, zsize):
            with open("./pics/" + img_title[i] + ".jpg", "wb") as imgf:
                zimg = req.get("https:" + img_src[i])
                imgf.write(zimg.content)
                imgf.close()

def reptile_2():
    zheader = {"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41"}
    #url = "https://baike.baidu.com/item/%E5%9B%BD%E9%99%85%E8%B6%B3%E8%81%94%E4%B8%96%E7%95%8C%E6%9D%AF/7872861"
    zurl = "https://vd3.bdstatic.com/mda-mbbeur0qh1p1x7u4/hd/h264/1613096924/mda-mbbeur0qh1p1x7u4.mp4"
    zvideo = req.get(zurl, headers=zheader)
    zvideo.raise_for_status()
    with open("./videos/WorldCupIntro.mp4", "wb") as vf:
        vf.write(zvideo.content)

"""
url0 = 'https://www.zhihu.com/question/352470379'
url1 = 'https://www.enterdesk.com/special/baidu/s'
url2 = 'http://xlzd.me'
url3 = 'http://www.baidu.com/s'
url4 = 'http://www.baidu.com/link?url=QeTRFOS7TuUQRppa0wlTJJr6FfIYI1DJprJukx4Qy0XnsDO_s9baoO8u1wvjxgqN'

#headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3947.100 Safari/537.36'}
#设置加入参数进行request
rparam = {'wd': '高达', 'rn': 100}
#设置headers伪装浏览器进行爬虫
header = {'User-Agent': 'just do it', 'Cookie': 'sucks'}
#设置request响应时长
timeout = 3
#设置代理IP进行访问
proxya = {
  "http": "http://10.10.1.10:3128",
  "https": "http://10.10.1.10:1080",
}
#设置带账户密码登录的代理IP进行访问
proxyb = {
  "http": "http://user:pass@10.10.1.10:3128",
}
#设置重定向开关allow_redirects
zstr = req.get(url3, params=rparam, headers=header, allow_redirects=True)
#zstr = req.get(url3, headers=headers)
print("headers: ", zstr.request.headers)
print('状态码:\n',zstr.status_code)
zt = etree.HTML(zstr.text)
#print(zstr.text, '\n{}\n'.format('*'*79), zstr.encoding)
print('URL:\n', zstr.url, '\nHeaders:\n', zstr.headers, '\nCookies:\n', zstr.cookies, '\nEncoding:\n', zstr.encoding, '\njson:\n', zstr.json)

#打印网页头
#print(zstr.headers['content-type'])
#print(zstr.content, '\n{}\n'.format('*'*79), zstr.encoding)

mdict = dict()
#知乎论坛问题
#mdict['问题'] = zt.xpath('//*[@class="QuestionHeader-title"]/text()')
#mdict['问题描述'] = zt.xpath('//*[contains(@class, "QuestionRichText")]//span/text()')
#mdict['问题回复'] = zt.xpath('*//text()')
#mdict['问题关注数'] = str(zt.xpath('//*[@class="NumberBoard-itemValue"]/text()')[0])
#mdict['问题浏览数'] = str(zt.xpath('//*[@class="NumberBoard-itemValue"]/text()')[1])
#'x'.join(y) 当y为元祖或者列表(字符串也能)时，能以x为间隔符号分割元素并去除引号和中括号输出


for key, value in mdict.items():
    print(hilight + key + dcolor)
    if(type(value) == type(str())):
        print(value)
    else:
        print("\n************\n".join(value))

"""
#here to run code
reptile_2()

