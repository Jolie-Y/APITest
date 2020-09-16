import requests

class HttpRequest:
    def http_request(self,url,params,header,http_method):
        res = ""
        if http_method.upper()=="POST":
            try:
                #print("---------------------")
                res = requests.post(url,json=params,headers=header)
                #print("post请求结束-------------------")
            except Exception as e:
                print("POST请求出现了异常:{0}".format(e))
        elif http_method.upper()=="GET":
            try:
                res = requests.get(url,params)
            except Exception as e:
                print("GET请求出现了异常：{0}".format(e))
        return res
