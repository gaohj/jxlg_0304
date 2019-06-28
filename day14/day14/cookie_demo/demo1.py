import urllib.request
from http import cookiejar
#创建文件用来保存cookie
filename = "qfedu.txt"
# 创建一个对象存储cookie
cookies = cookiejar.LWPCookieJar(filename=filename) #跟文件交互一般用这个
#cookies = cookiejar.CookieJar()
# cookie处理器, 提取cookie
cookie_handler = urllib.request.HTTPCookieProcessor(cookies)
# 创建打开器, 处理cookie
opener = urllib.request.build_opener(cookie_handler)

headers = {
    "User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}

url="http://www.so.com/"
#创建请求对象
req=urllib.request.Request(url,headers=headers)

response = opener.open(req)
cookies.save()
