#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import json


def request_api(url, data, headers):
    """
    请求接口
    :param url:
    :param data:
    :param headers:
    :return:
    """
    try:
        res = requests.post(url, data=data, headers=headers)
        content = res.content.decode(encoding='utf-8')
        content = json.loads(content)
        if content['code']:
            return False
        # 返回数据
        data = content['data']
    except Exception:
        return False
    return data
