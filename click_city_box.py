#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from config import *
from function import *
import pymysql

ad_box_url = BASE_API_URL + 'grid/get-list'
click_url = BASE_API_URL + 'grid/detail'

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
search_sql = 'select code,lng,lat from region where code > 6590'
cursor.execute(search_sql)
city_list = cursor.fetchall()
cursor.close()
connect.close()

for k, v in enumerate(city_list):
    data = 'city_id=' + str(v[0]) + '&page=1'
    res = request_api(ad_box_url, data, headers)
    try:
        if not res['list']:
            continue
    except Exception:
        continue
    for kk, vv in enumerate(res['list']):
        if vv['img']:
            click_data = 'city_id=' + str(v[0]) + '&grid_id=' + vv['grid_id'] + '&longitude=' + v[1] + '&latitude=' + v[2]
            print(click_data)
            try:
                detail = request_api(click_url, click_data, headers)
            except Exception:
                continue
        else:
            continue