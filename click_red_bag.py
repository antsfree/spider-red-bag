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


def update_user_info(uid, user_money):
    """
    更新用户信息
    :param uid:
    :param user_money:
    :return:
    """
    try:
        update_connect = pymysql.Connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            db=DB_DATABASE,
            charset=DB_CHARSET
        )
        update_cursor = update_connect.cursor()
        update_sql = 'update user_info set user_money=' + str(user_money) + ' where uid=' + str(uid)
        try:
            update_cursor.execute(update_sql)
            # 提交
            update_connect.commit()
            update_cursor.close()
            update_connect.close()
        except Exception:
            return False
    except Exception:
        return False


def open_adv_red_bag(ad_list):
    """
    拆广告红包
    :param ad_list:
    :return:
    """
    for detail in ad_list:
        # click red bag
        try:
            type_one_click_url = BASE_API_URL + 'redbag/click'
            type_one_click_data = 'type=1&longitude=' + request_header['longitude'] + '&latitude=' + request_header[
                'latitude'] + '&id=' + detail['id'] + '&uid=' + request_header['uid']
            type_one_click_response = request_api(type_one_click_url, type_one_click_data, request_header)
            # open red bag
            type_one_open_url = BASE_API_URL + 'redbag/receive'
            type_one_open_data = 'uid=' + request_header['uid'] + '&sign=' + type_one_click_response['sign'] + '&id=' + detail[
                'id']
            request_api(type_one_open_url, type_one_open_data, request_header)
        except Exception:
            return False


# 红包列表路由
red_bag_list_url = BASE_API_URL + 'redbag/redbag-list'
# 持续执行 sleep&enumerate
while 1:
    # 用户 header 头列表，每次循环重新请求获取
    header_list = return_user_header_list()
    # sleep_time 参数设置
    next_time_list = []
    sleep_time = 10
    # 循环用户入参列表，实现多用户切换取值
    for request_header in header_list:
        red_bag_list_request_data = 'type=2&longitude=' + request_header['longitude'] + '&latitude=' + request_header[
            'latitude'] + '&id=1&uid=' + request_header['uid']
        response = request_api(red_bag_list_url, red_bag_list_request_data, request_header)
        # print(response)
        try:
            # IO优化，获取最小 next_time 作为 sleep_time
            next_time_list.append(int(response['next_time']))
            # 广告红包和系统红包的处理
            type_one_list = type_two_list = []
            for k, v in enumerate(response['list']):
                # 广告红包 type=1
                if v['type'] == 1:
                    type_one_list.append(v)
                # 系统红包 type=2
                elif v['type'] == 2:
                    type_two_list.append(v)
            if type_one_list:
                # 广告红包直接点击掉
                open_adv_red_bag(type_one_list)
            # 系统红包处理
            list_num = len(type_two_list)
            # 更新用户余额(会慢一步更新)
            # TODO 更新用户next_time，优化 IO
            update_user_info(request_header['uid'], response['user_money'])
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
        search_sql = 'select id,red_bag_id,sign from red_bag where uid = ' + request_header[
            'uid'] + ' order by money desc limit ' + str(iterating_num)
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
            # print(delete_ids)
            continue
        # delete
        delete_clicked_red_bag(delete_ids)
        # !!强制更新 next_time
        request_api(red_bag_list_url, red_bag_list_request_data, request_header)
    # 所有用户扫一遍后，进入最小休眠周期
    if next_time_list:
        sleep_time = min(next_time_list)
    # print(sleep_time)
    try:
        time.sleep(int(sleep_time))
    except Exception:
        time.sleep(10)
