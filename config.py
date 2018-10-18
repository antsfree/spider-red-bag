#!/usr/bin/env python3
# -*- coding: utf-8 -*-
DB_HOST = 'localhost'
DB_PORT = 3306
DB_USER = 'root'
DB_PASSWORD = '123456'
DB_DATABASE = 'redbag'
DB_CHARSET = 'utf8'

# 接口 URL
BASE_API_URL = 'http://bdhb.shuangpinkeji.com/api/m1/'

Authorization = 'eyJ1aWQiOjQyNjQwOCwidGltZXN0YW1wIjoxNTM5NjY4MTU3LCJzaWduIjoiOWQ4ODU2Nzc2OGY3MDAwMmFhYjFjMWEzMDhiYThhOGIifQ=='
ContentType = 'application/x-www-form-urlencoded'
Cookie = 'acw_tc=65c86a0915384935029466871e42f346f2e9c2825d8f7b7576115232e2efc0; _csrf=4cac69565cef09502f1f30f3334e99173f4fb7a6c5be45d96b4ac1e0be50a758a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22u7X8YNS5gIXjGuFKMR5lGYyBsr9N3Id-%22%3B%7D'

headers = {
    'Authorization': Authorization,
    'Content-Type': ContentType,
    'Cookie': Cookie
}