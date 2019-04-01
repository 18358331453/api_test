#coding=utf-8
import requests
import threading


def test_req_01(i):
    requrl='http://192.168.45.191//api/dayan/project/enregister/ope'
    token=["eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOiIxMTAyNzc4ODM3MDIyMzEwNDAyIiwiaXNzIjoiZGF5YW4iLCJleHAiOjE1NTE5MzEwNjMsIl8iOjE1NTE3NTgyNjM4NjB9.PM5F8XIvZf2Pi5d1w4YgaApUi8nFOQh6AzlumRdTDWI",
           "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOiIxMTAyODAyNzIyMjMzMDI0NTE0IiwiaXNzIjoiZGF5YW4iLCJleHAiOjE1NTE5MzY0MzIsIl8iOjE1NTE3NjM2MzI3Njh9.rtyy-wgc7ETlH6QoP4xTLnSuP2OhoKNfnarVsbop2Zc"]
    headers={
        "Content-Type":"application/json",
        "token":token[i]
    }
    data={
        "productId":"456",
        "togetherId":"1102774633784049666",
        "enregisterShare":"10",
        "isAutoSurvival":"2"
    }
    r=requests.post(requrl,json=data,headers=headers)
    print(r.text)
thread=[]
for i in range(2):
    t1=threading.Thread(target=test_req_01,args=(i,))
    thread.append(t1)

if __name__=='__main__':
    for t in thread:
        t.setDaemon(True)
        t.start()

    for t2 in thread:
        t2.join()
    print('所有线程结束')