# -*- encoding: utf-8 -*-
# @Time    : 2019/7/24 21:37
# @Author  : mike.liu
# @File    : Locust_post.py
import json
import random

from locust import TaskSet, task, HttpLocust


class ApiLogin(TaskSet):
    # 登录

    @task()
    def login(self):
        with open("D:\\python\\locust\\mobile.txt") as f:
            mobile_id = f.readlines()
        mobile_ids = []
        # readlines获取每一行数据保存为list，每一行数据是一个元素，字符串形式，
        # 这里变量转为int 可以去掉换行符号在append一个新数组

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
        self.client.post("/mobile/api/user/login", data, headers=headers)


class WebsiteUser(HttpLocust):
    task_set = ApiLogin
    min_wait = 3000  # 单位时间
    max_wait = 6000  # 单位毫秒
    stop_timeout = 300  # 设置多少秒停止，是这个场景要跑多长的时间
    host = "http://192.168.226.130:8080"


if __name__ == "__main__":
    import os
    # 启动locust
    os.system("locust -f Locust_post.py WebsiteUser")
