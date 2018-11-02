#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from config import *
from function import *
from user_info import return_user_header_list
from region import fetch_all_region
import time
from email_message import send_email

# 区县列表
city_list = fetch_all_region()

while 1:
    # 执行时间过滤
    now_clock = time.localtime().tm_hour
    if now_clock not in (1, 14):
        time.sleep(1800)
        continue
    send_email('脚本启动: ')
    # 用户 header 头列表
    header_list = return_user_header_list()
    ad_box_url = BASE_API_URL + 'grid/get-list'
    click_url = BASE_API_URL + 'grid/detail'
    for k, v in enumerate(city_list):
        data = 'city_id=' + str(v[0]) + '&page=1'
        res = request_api(ad_box_url, data, header_list[0])
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
                    for request_header in header_list:
                        detail = request_api(click_url, click_data, request_header)
                except Exception:
                    continue
            else:
                continue
    send_email('脚本已经跑完, 进入下个周期: ')
