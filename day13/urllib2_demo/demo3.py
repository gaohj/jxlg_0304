#encoding:utf-8
import os
import urllib2
import urllib
#urllib仅仅能接受url 能用urlencode 编码  urllib.urlencode
def baidu_search(params):
    headers = {
        "User-Agent": "User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
    }

    #https://www.baidu.com/s?wd=xcxk
    url = "http://www.baidu.com/s?"+params
    #创建请求对象
    req = urllib2.Request(url,headers=headers)
    response = urllib2.urlopen(req)

    print response.read()#读取内容

    dir = './'
    os.chdir(dir)
    file = urllib2.urlopen(url).read()
    open('baidu.html','wb').write(file)
    print "ok"

if __name__ == "__main__":
    kw = raw_input("请输入要查找的内容")
    params = {
        'wd':kw
    }

    params = urllib.urlencode(params)

    baidu_search(params)
