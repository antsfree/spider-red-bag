#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from config import *
import pymysql


def fetch_all_region():
    """
    获取全部区县信息
    :return:
    """
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
    city_res = cursor.fetchall()
    cursor.close()
    connect.close()

    return city_res
