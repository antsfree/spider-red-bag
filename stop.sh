#!/bin/sh

# 先清除进程
pkill -f receive_red_bag.py
pkill -f click_city_box.py
pkill -f click_red_bag.py

echo '进程清除完成!'