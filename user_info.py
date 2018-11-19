from config import *
import pymysql
from function import request_api


def get_user_list(field='*'):
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
    search_sql = 'select ' + field + ' from user_info where is_delete = 0'
    cursor.execute(search_sql)
    user_list = cursor.fetchall()
    cursor.close()
    connect.close()

    return user_list


def return_user_header_list():
    user_list = get_user_list()
    user_headers = []
    for k, v in enumerate(user_list):
        user_headers.append(
            {
                'uid': v[1],
                'Authorization': v[3],
                'Cookie': v[4],
                'Content-Type': 'application/x-www-form-urlencoded',
                'longitude': v[5],
                'latitude': v[6]
            }
        )
    return user_headers


def user_login(uid):
    user_list = get_user_list()
    for k, v in enumerate(user_list):
        # login
        if v[1] == str(uid):
            login_url = BASE_API_URL + 'auth/login'
            login_data = v[9]
            login_head = {
                'uid': v[1],
                'Authorization': v[3],
                'Cookie': v[4],
                'Content-Type': 'application/x-www-form-urlencoded',
                'longitude': v[5],
                'latitude': v[6]
            }
            response = request_api(login_url, login_data, login_head)
            try:
                token = response['token']
                update_connect = pymysql.Connect(
                    host=DB_HOST,
                    port=DB_PORT,
                    user=DB_USER,
                    password=DB_PASSWORD,
                    db=DB_DATABASE,
                    charset=DB_CHARSET
                )
                update_cursor = update_connect.cursor()
                update_sql = 'update user_info set authorization="' + str(token) + '" where uid=' + str(uid)
                update_cursor.execute(update_sql)
                # 提交
                update_connect.commit()
                update_cursor.close()
                update_connect.close()
                return True
            except Exception:
                return False
