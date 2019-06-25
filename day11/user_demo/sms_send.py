#encoding:utf-8

#pip install requests
import requests

def send(mobile,captcha):
    url = 'http://v.juhe.cn/sms/send'
    params = {
        "mobile":mobile,
        "tpl_id":135629,
        "tpl_value":"#code#="+captcha,
        "key":"",
    }

    response = requests.get(url=url,params=params)
    result = response.json()
    print(result)
    if result['error_code'] == 0:
        return True
    else:
        return False

send(111,'beauty')