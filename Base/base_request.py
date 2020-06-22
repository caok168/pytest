# coding=utf-8
import json

import requests


class BaseRequest:
    def send_post(self, url, data):
        res = requests.post(url=url, data=data).text()
        return res

    def send_get(self, url, data):
        res = requests.get(url=url, params=data).text()
        return res

    def run_main(self, method, url, data):
        if method == 'get':
            res = self.send_get(url, data)
        else:
            res = self.send_post(url, data)
        try:
            res = json.loads(res)
        except:
            print("this res is text")
        return res
