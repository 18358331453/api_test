#coding=utf-8
import requests

#传手机号登录，然后返回一个带token的headers
def get_headers(telphone=18358331453):
    s=requests.session()
    #登录前要先请求发送验证码
    url_getcode="http://192.168.100.142//api/dayan/user/login/getVCode/"+str(telphone)
    r=s.get(url_getcode)
    assert r.json()['message'] =='请求成功' ,"验证码获取失败"
    #请求发送验证码后再登录
    url_login="http://192.168.100.142//api/dayan/user/login"
    data={
        "code": "888888",
        "phoneNumber":str(telphone),
        "registerChannelId": "",
        "invitationUid": ""
    }
    r=s.post(url_login,json=data)
    assert r.json()['message'] =='请求成功' ,"注册/登录操作失败"
    headers={"Content-Type":"application/json",
             "token":r.headers['token']
             }
    return headers

def get_token():
    s=requests.session()
    #登录前要先请求发送验证码
    url_getcode="http://192.168.100.142//api/dayan/user/login/getVCode/18358331453"
    r=s.get(url_getcode)

    url_login="http://192.168.100.142//api/dayan/user/login"
    data={
        "code": "888888",
        "phoneNumber": "18358331453",
        "registerChannelId": "",
        "invitationUid": ""
    }

    r=s.post(url_login,json=data)
    print(r.text)
    return r.headers['token']


# get_headers()