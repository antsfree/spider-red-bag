#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from config import *
import pymysql
import time
import random
from function import *


def insert_red_bag(data, request_headers, min_money='0.0450'):
    """
    插入红包数据
    :param data:
    :param request_headers:
    :param min_money:
    :return:
    """
    # 随机休眠
    # sleep_time = random.randint(2, 5)
    # time.sleep(sleep_time)
    # 请求路由
    click_red_bag_url = BASE_API_URL + 'redbag/click'
    # 获取红包信息
    red_bag_info = request_api(click_red_bag_url, data, request_headers)
    # 数据处理
    connect = pymysql.Connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        db=DB_DATABASE,
        charset=DB_CHARSET
    )
    cursor = connect.cursor()
    if red_bag_info['money'] < min_money:
        return False
    insert_str = 'insert into red_bag (`sign`,`red_bag_id`,`uid`,`money`,`stock_num`,`type`) values ("' + red_bag_info[
        'sign'] + '","' + str(red_bag_info['id']) + '","' + str(red_bag_info['uid']) + '","' + red_bag_info[
                     'money'] + '","' + str(red_bag_info['stock_num']) + '","' + str(red_bag_info['type']) + '")'

    cursor.execute(insert_str)
    insert_id = connect.insert_id()
    # 提交
    connect.commit()
    return insert_id


# 不同的用户不同的请求数据
request_data = 'type=2&longitude=118.75538719&latitude=31.97804634&id=1&uid=426408'

for i in range(1, 10000):
    res = insert_red_bag(request_data, headers)
    print(res)
