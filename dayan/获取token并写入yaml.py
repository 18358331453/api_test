#coding=utf-8
import requests
import os
import yaml

cur_path = os.path.dirname(os.path.realpath(__file__))


def get_token():
    s=requests.session()
    #登录前要先请求发送验证码
    url_getcode="http://192.168.45.191//api/dayan/user/login/getVCode/18358331453"
    s.get(url_getcode)

    url_login="http://192.168.45.191//api/dayan/user/login"
    data={
        "code": "888888",
        "phoneNumber": "18358331453",
        "registerChannelId": "1075951745682427907",
        "invitationUid": ""
    }

    r=s.post(url_login,json=data)
    return r.headers['token']

def write_yaml(token):
    yaml_path=os.path.join(cur_path,'common','token.yaml')
    data={"token":token}
    with open(yaml_path, "w", encoding="utf-8") as f:
        yaml.dump(data,f)

if __name__=="__main__":
    write_yaml(get_token())