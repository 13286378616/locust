# -*- encoding: utf-8 -*-
# @Time    : 2019/7/24 21:02
# @Author  : mike.liu
# @File    : locust_get.py
from locust import TaskSet, task, HttpLocust


'''新建一个类LocustApi(TaskSet)，继承TaskSet，该类定义了每个用户的任务组合，测试任务开始后，
每个locust会从Taskset中随机挑选一个任务执行，然后随机等待httplocust类中定义的min_wait和max_wait
之间的一段时间执行下一个任务
'''


class LocustApi(TaskSet):
    # 获取商品列表
    # 装饰该方法表示为用户行为，括号里面参数表示该行为的执行权重，数值越大，执行频率越高，默认是1
    @task()
    def get_types(self):
        # self.client调用get或者post方法，和requests一样
        response = self.client.get("/mobile/api/goods/gettypes")
        result = response.json()

        # 断言
        assert result['code'] == 0
        if result['code'] == 0:
            print('Pass_get')
        else:
            print('Fail_get')


class WebsiteUser(HttpLocust):
    # 指向定义了用户行为的类
    task_set = LocustApi
    min_wait = 3000     # 单位时间
    max_wait = 6000     # 单位毫秒
    # stop_timeout = 60000
    host = "http://192.168.226.130:8080"


if __name__ == "__main__":
    import os
    # --host:指定服务器的域名地址
   # os.system("locust -f locust_get.py --host=http://192.168.226.130:8080")
    os.system("locust -f locust_get.py --slave --master-host=192.168.226.130")
