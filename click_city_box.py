#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from config import *
from function import *
from user_info import return_user_header_list
from region import fetch_all_region
import time

# 区县列表
city_list = fetch_all_region()

while 1:
    # 用户 header 头列表
    header_list = return_user_header_list()
    for request_header in header_list:
        ad_box_url = BASE_API_URL + 'grid/get-list'
        click_url = BASE_API_URL + 'grid/detail'
        for k, v in enumerate(city_list):
            data = 'city_id=' + str(v[0]) + '&page=1'
            res = request_api(ad_box_url, data, request_header)
            try:
                if not res['list']:
                    continue
            except Exception:
                continue
            for kk, vv in enumerate(res['list']):
                if vv['img']:
                    click_data = 'city_id=' + str(v[0]) + '&grid_id=' + vv['grid_id'] + '&longitude=' + v[
                        1] + '&latitude=' + v[2]
                    # print(click_data)
                    try:
                        detail = request_api(click_url, click_data, request_header)
                    except Exception:
                        continue
                else:
                    continue
    # 所有用户跑完之后休眠一个小时
    # time.sleep(3600)
