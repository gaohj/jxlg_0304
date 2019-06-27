#encoding:utf-8

from urllib import request
import urllib.parse  #能够通过 urlencode 进行编码

#python2 的urllib2 到python3 成了 urllib.request

headers = {
    "User-Agent":"User-Agent,Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
}

kw = input("请输入关键字:")
params = {
    'wd':kw
}

params = urllib.parse.urlencode(params)
print(params) #浏览器不识别中文

#创建url
url = 'http://www.baidu.com/s?'+params

#创建请求对象
requests = urllib.request.Request(url,headers=headers)
response = urllib.request.urlopen(requests)


# print(response.read().decode('utf-8'))
print(response.status)
print(response.__dict__)