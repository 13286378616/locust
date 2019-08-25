# -*- encoding: utf-8 -*-
# @Time    : 2019/7/24 22:27
# @Author  : mike.liu
# @File    : api_get_post.py
from locust import TaskSet, HttpLocust, task
import json
import random


class LocustApi(TaskSet):
    # 获取商品列表
    @task(1)
    def get_types(self):
        response = self.client.get("/mobile/api/goods/gettypes")
        result = response.json()
        # 断言
        assert result['code'] == 0
        if result['code'] == 0:
            print('Pass_get')

        else:
            print('Failure!')

    @task(2)
    def login(self):
        with open("D:\\python\\locust\\mobile.txt") as f:
            mobile_id = f.readlines()
        mobile_ids = []
        # readlines获取每一行数据保存为list，每一行数据是一个元素，字符串形式，
        # 这里要遍历转为int可以去掉换行符号再append一个新数组。

        for i in mobile_id:
            data = int(i)
            mobile_ids.append(data)
        ran = random.randint(0, 5)
        # 随机取出一个数据
        mobile_id = mobile_ids[ran]
        mobile = str(mobile_id)
        headers = {'content-type': 'application/json'}
        params = {"mobile": mobile, "password": "123456"}
        data = json.dumps(eval(str(params)))
        data = data.encode('utf-8')
        response = self.client.post("/mobile/api/user/login", data, headers=headers)
        result = response.json()
        # 断言
        # assert result['code'] == 0
        if result['code'] == 0:
            print('Pass_post')

        else:
            print('Failure!')


class WebsiteUser(HttpLocust):
    task_set = LocustApi
    min_wait = 3000  # 单位毫秒
    max_wait = 6000  # 单位毫秒
    host = "http://192.168.226.130:8080"


if __name__ == "__main__":
    import os

    # 启动locust，
    os.system("locust -f api_get_post.py  WebsiteUser")
