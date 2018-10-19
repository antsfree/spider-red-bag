#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from config import *
import pymysql
from function import *
import time
import random
from user_info import return_user_header_list


def click_red_bag(re_sign, re_id, uid, re_headers):
    """
    点击红包
    :param re_sign:
    :param re_id:
    :param uid:
    :param re_headers:
    :return:
    """
    # click red bag
    click_url = BASE_API_URL + 'redbag/sys-receive'
    red_bag_info = 'uid=' + str(uid) + '&sign=' + str(re_sign) + '&id=' + str(re_id) + '&type=2'
    res = request_api(click_url, red_bag_info, re_headers)
    return res


def delete_clicked_red_bag(del_ids=''):
    """
    删除作废红包
    :param del_ids:
    :return:
    """
    if not del_ids:
        return False
    # delete
    del_connect = pymysql.Connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        db=DB_DATABASE,
        charset=DB_CHARSET
    )
    del_cursor = del_connect.cursor()
    delete_sql = 'delete from red_bag where id in (' + del_ids + ')'
    del_cursor.execute(delete_sql)
    del_connect.commit()
    del_cursor.close()
    del_connect.close()


# 红包列表路由
red_bag_list_url = BASE_API_URL + 'redbag/redbag-list'
# 用户 header 头列表
header_list = return_user_header_list()
# 持续执行 sleep&enumerate
while 1:
    # 循环用户入参列表，实现多用户切换取值
    for request_header in header_list:
        red_bag_list_request_data = 'type=2&longitude=' + request_header['longitude'] + '&latitude=' + request_header[
            'latitude'] + '&id=1&uid=' + request_header['uid']
        response = request_api(red_bag_list_url, red_bag_list_request_data, request_header)
        try:
            list_num = len(response['list'])
        except Exception:
            list_num = 0
        if list_num <= 1:
            continue
        iterating_num = list_num - 1
        # 查表
        connect = pymysql.Connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            db=DB_DATABASE,
            charset=DB_CHARSET
        )
        cursor = connect.cursor()
        search_sql = 'select id,red_bag_id,sign from red_bag order by money desc limit 1'
        cursor.execute(search_sql)
        sign_list = cursor.fetchall()
        cursor.close()
        connect.close()
        # 删除
        del_list = []
        for k, v in enumerate(sign_list):
            del_list.append(str(v[0]))
            # click red bag
            click_res = click_red_bag(v[2], v[1], request_header['uid'], request_header)
        delete_ids = ','.join(del_list)
        if not delete_ids:
            continue
        # delete
        delete_clicked_red_bag(delete_ids)
        # !!强制更新 next_time
        request_api(red_bag_list_url, red_bag_list_request_data, request_header)
    # 所有用户扫一遍后，进入随机休眠
    time.sleep(random.randint(60, 120))
