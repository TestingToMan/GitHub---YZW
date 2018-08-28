import urllib
import urllib.request
import re
import json
import socket
import urllib.request
import urllib.parse
import urllib.error
import time
# time.out = 10
# socket.setdefaulttimeout(timeout)

# 打开网页，下载器
def open_html(url):
    require = urllib.request.Request(url)
    reponse = urllib.request.urlopen(require)
    html = reponse.read()
    return html
# 下载图片
def load_image(html):
    regx = 'https?://[\S]*.jpg'
    pattern = re.compile(regx)
    get_image = re.findall(pattern, repr(html))

    num = 1
    for img in get_image:
        photo = open_html(img)

        with open(r'/Users/yangzewei/Crawler_P/%s.jpg' % num, 'wb') as f:
            print('开始下载图片')
            f.write(photo)
            print('正在下载第%s张图片' % num)
            f.close()

        num = num + 1
        if num <= 100:
            print('go on')
            # print(get_image)
        else:
            break
    if num == 100:
        print('全部下载成功！！！')
    else:
        print('下载完成！')


url = 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=index&fr=&hs=0&xthttps=111111&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E9%99%88%E5%A5%95%E8%BF%85%E6%B5%AE%E5%A4%B8&oq=%E9%99%88%E5%A5%95%E8%BF%85%E6%B5%AE%E5%A4%B8&rsp=-1'
html = open_html(url)
load_image(html)