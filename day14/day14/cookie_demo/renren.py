import urllib.request
from http import cookiejar

cookies = cookiejar.CookieJar()
# cookie处理器, 提取cookie
cookie_handler = urllib.request.HTTPCookieProcessor(cookies)
# 创建打开器, 处理cookie
opener = urllib.request.build_opener(cookie_handler)
url = "http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2019551613453"


data = {
    "email": "gaohj5@163.com",
    "icode": "",
    "origURL": "http://www.renren.com/home",
    "domain": "renren.com",
    "key_id": "1",
    "captcha_type": "web_login",
    "password": "357eec1f0e33a6d8166188b103eaa38357ca2ba9953b3443993e0b6f02f18463",
    "rkey": "cb15f985754fd884a44506ff5db1256e",
    "f": "http%3A%2F%2Fwww.renren.com%2F541197383",
}


headers = {
    "Referer": "http://www.renren.com/SysHome.do",
    "Origin": "http://www.renren.com",
    "Host": "www.renren.com",
    "User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}

req = urllib.request.Request(url,headers=headers,data=data)
response = opener.open(req)
print(response.read().decode('utf-8'))

url2 = "http://www.renren.com/541197383"
headers1 = {
    "User-Agent": "User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}

reqs = urllib.request.Request(url2,headers=headers1)
response = opener.open(req)
with open('renren.html','wb',encoding='utf-8') as fp:
    fp.write(response.read().decode('utf-8'))