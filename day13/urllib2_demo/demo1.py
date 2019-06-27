#encoding:utf-8
import urllib2

url = 'http://www.baidu.com/'

#data为none 说明这是get请求 否则就是post 请求
res = urllib2.urlopen(url=url,data=None)

# print(res)
# print(res.read()) #返回的是所有的内容
# print res.readline() #第一行
# print res.readlines() #所有的行
# print res.getcode()
# print res.geturl()
# print res.code

print res.read().decode('utf-8')