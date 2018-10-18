#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from config import *
import pymysql
from function import *

red_bag_list_url = BASE_API_URL + 'redbag/redbag-list'
data = 'longitude=118.762329&latitude=31.97537711&uid=426408'


def get_red_bag_list(url, data, headers):
    response = request_api(url, data=data, headers=headers)
    try:
        list_num = len(response['list'])
        # next_time = response['next_time']
    except Exception:
        list_num = 0
    return list_num


list_num = get_red_bag_list(red_bag_list_url, data, headers)
if list_num <= 1:
    exit()
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
search_sql = 'select id,red_bag_id,sign from red_bag order by money desc limit ' + str(iterating_num)
cursor.execute(search_sql)
sign_list = cursor.fetchall()
cursor.close()
connect.close()

l = []
for k, v in enumerate(sign_list):
    l.append(str(v[0]))
    # click red bag
    click_url = BASE_API_URL + 'redbag/sys-receive'
    red_bag_info = 'uid=426408&sign=' + v[2] + '&id=' + v[1] + '&type=2'
    res = request_api(click_url, red_bag_info, headers)

delete_ids = ','.join(l)
if not delete_ids:
    exit()
# delete
cursor = connect.cursor()
search_sql = 'delete from red_bag where id in (' + delete_ids + ')'
cursor.execute(search_sql)
connect.commit()
cursor.close()
connect.close()
