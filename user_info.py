from config import *
import pymysql


def get_user_list(field = '*'):
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
