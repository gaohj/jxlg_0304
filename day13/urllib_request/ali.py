#encoding:utf-8
import json
import urllib.parse
from urllib import request



headers = {
    "User-Agent":"User-Agent,Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
}

url = "http://job.alibaba.com/zhaopin/socialPositionList/doList.json"

for i in  range(1,20):
    params = {
        "pageSize":10,
        "t":"0.8991060863969329",
        "PageIndex":i
    }

    data = urllib.parse.urlencode(params).encode()
    req = urllib.request.Request(url, headers=headers,data=data)

    response = urllib.request.urlopen(req)
    content = response.read().decode()

    print(content)

    data_dict = json.loads(content)
    print(data)

    job_list = data_dict['returnValue']['datas']

    for job in job_list:
        degree = job.get('degree')
        requirement = job.get('requirement')
        workExperience = job.get('workExperience')
        description = job.get('description')
        firstCategory = job.get('firstCategory')

        with open('ali.txt','a+',encoding='utf-8') as fp:
            fp.write(str((degree,requirement,workExperience,description,firstCategory))+"\n")
