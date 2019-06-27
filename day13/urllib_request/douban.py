#encoding:utf-8
import json
import urllib
from urllib import request



headers = {
    "User-Agent":"User-Agent,Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
}

for i in range(100):
    url = "https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start=%d" % i
    req = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(req)
    content = response.read().decode()

    #解析json

    data = json.loads(content)
    print(data)

    data_list = data.get('data')

    for movie in data_list:
        title = movie['title']
        casts = movie['casts']
        rate = movie['rate']

        with open('douban.txt','a+',encoding='utf-8') as fp:
            fp.write(str((title,casts,rate))+"\n")


