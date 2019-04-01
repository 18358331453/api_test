#coding=utf-8
import requests
from dayan.common.get_token import get_token
from dayan.common.login import get_headers

headers=get_headers()
url_getinfo="http://192.168.45.191//api/dayan/user/relevant/info"
r=requests.get(url_getinfo,headers=headers)
print(r.text)
assert r.json()['data']['headImgUrl'] == None
