#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from config import *
import pymysql
import time
import random
from function import *

click_red_bag_url = BASE_API_URL + 'redbag/click'
headers = {
    'Authorization': Authorization,
    'Content-Type': ContentType,
    'Cookie': Cookie
}
data = 'type=2&longitude=118.75538719&latitude=31.97804634&id=1&uid=426408'


def insert_red_bag(red_bag_info):
    connect = pymysql.Connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        db=DB_DATABASE,
        charset=DB_CHARSET
    )
    cursor = connect.cursor()
    insert_str = 'insert into red_bag (`sign`,`red_bag_id`,`uid`,`money`,`stock_num`,`type`) values ("' + red_bag_info[
        'sign'] + '","' + str(red_bag_info['id']) + '","' + str(red_bag_info['uid']) + '","' + red_bag_info[
                     'money'] + '","' + \
                 str(red_bag_info['stock_num']) + '","' + str(red_bag_info['type']) + '")'

    cursor.execute(insert_str)
    insert_id = connect.insert_id()
    # 提交
    connect.commit()
    return insert_id


for i in range(1, 10000):
    # 获取红包信息
    red_bag_info = request_api(click_red_bag_url, data, headers)
    res = insert_red_bag(red_bag_info)
    sleep_time = random.randint(0, 1)
    time.sleep(sleep_time)
    # print(str(sleep_time) + '--' + str(res))
