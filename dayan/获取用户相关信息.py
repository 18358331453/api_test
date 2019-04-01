#coding=utf-8
import requests
from dayan import get_token


headers={"Content-Type":"application/json",
         "token":get_token.get_token()
         }

url_getinfo="http://192.168.45.191//api/dayan/user/relevant/info"
r=requests.get(url_getinfo,headers=headers)
print(r.text)
assert r.json()['data']['headImgUrl'] == None
