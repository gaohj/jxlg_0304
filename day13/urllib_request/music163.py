#encoding:utf-8
import json
import urllib.parse
from urllib import request
headers = {
    "User-Agent":"User-Agent,Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
}
url = "https://music.163.com/weapi/v1/resource/comments/A_PL_0_2813436003?csrf_token="

params = {
    "params":"jMsYvbVz788vBNv4PXaLVwnj1ymX/nK4ji+0/mHd2ymwBhGUXuK80sX3UKA85fDF0sGzKPpYVm9flEuTFEZjy40hao2I+kEtYbP0TmysGbOJgvbDSnx5GaDJNSoTMu5Oy9Zw+70i2eoc9qXFDDUqxAow4IbwYUVsRPJjC1iJ5/gfQL4nA82zrcermHw7SqS9fveWzSO2M6IY/XLqTSkFk4jL8CZrhWnGDnTRZxpVguU=",
    "encSecKey":"08cdb864375b23753d0f7cc905f1a7365be3a33130340b80d507dd034989cb852a682e498921713a6c6d89d909a1764beb0785a205d6691d8501b975d90d702debf823149bbc6ca1c32d5809de9c93f4a846f62dcb84c1d8d40788250db845cd0b394d0338e00d64edf0f565d8eec76280cc3754b86b0fecd77b16e1fc05455f",

}

data = urllib.parse.urlencode(params).encode()

req = urllib.request.Request(url, headers=headers,data=data)
response = urllib.request.urlopen(req)
content = response.read().decode()

data_dict = json.loads(content)
print(data_dict['hotComments'])

hotComments= data_dict['hotComments']

for hotComment in  hotComments:
    nickname = hotComment['user']['nickname']
    content = hotComment['content']

    print(nickname,":",content)