from urllib import request
import base64
from zlib import decompress
import os
import config
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
    res = requests.post(url, data=data, headers=headers)
    content = res.content.decode(encoding='utf-8')
    content = json.loads(content)
    if content['code']:
        print('请求出错')
        exit()
    # 返回数据
    data = content['data']
    return data
