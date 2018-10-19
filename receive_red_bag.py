#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from config import *
import pymysql
import time
import random
from function import *
from user_info import return_user_header_list


def insert_red_bag(data, request_headers, min_money='0.0450'):
    """
    插入红包数据
    :param data:
    :param request_headers:
    :param min_money:
    :return:
    """
    # 随机休眠
    # sleep_time = random.randint(1, 3)
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
    try:
        if not red_bag_info['money']:
            return False
    except Exception:
        return False
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


def main():
    # 用户 header 头列表
    header_list = return_user_header_list()
    for request_header in header_list:
        # 不同的用户不同的请求数据
        request_data = 'type=2&longitude=' + request_header['longitude'] + '&latitude=' + request_header[
            'latitude'] + '&id=1&uid=' + request_header['uid']
        res = insert_red_bag(request_data, request_header)
        # if res:
        #     print(res)


if __name__ == '__main__':
    while 1:
        main()
        time.sleep(0.1)
