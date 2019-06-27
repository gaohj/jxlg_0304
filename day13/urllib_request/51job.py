#encoding:utf-8

import re
import urllib
from urllib import request



headers = {
    "User-Agent":"User-Agent,Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
}

#获取前程无忧的职位列表网址
url = "https://search.51job.com/list/130200%252C040000,000000,0000,00,9,99,Python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="

#开始爬取

req = urllib.request.Request(url,headers=headers)

response = urllib.request.urlopen(req)
html = response.read().decode('gbk')

# print(html)

jobnum_re = '<div class="rt">(.*?)</div>'

jobcomp = re.compile(jobnum_re,re.S) #re.S整个字符串都要匹配到
jobnums = jobcomp.findall(html)

print(jobnums[0])
num_re = ".*?(\d+).*"
num = re.findall(num_re,jobnums[0])
print(num)
print(num[0])
print(int(num[0]))


re_str = '<div class="el">(.*?)</div>'
job_list = re.findall(re_str,html,re.S)
print(job_list[0]) #这是第一个岗位的信息

res_str1 = 'onmousedown="">(.*?)</a>'
job_list2 = re.findall(res_str1,job_list[0],re.S)

print("第一个岗位的名称:%s" % job_list2[0].strip())

for job in job_list:
    res_str2 = 'onmousedown="">(.*?)</a>'
    job_list3 = re.findall(res_str2,job,re.S)
    print(job_list3[0].strip())