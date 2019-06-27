#encoding:utf-8

import urllib2

headers = {
    "User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}

url = "http://www.baidu.com"


#创建请求对象
req = urllib2.Request(url,headers=headers)

print req.get_full_url()
print req.get_method()
print req.get_header('User-Agent')
print req.get_host()
print req.get_type()
req.add_header("Connection","keep-alive")
print req.get_header('Connection')