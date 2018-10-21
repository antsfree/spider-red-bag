#!/bin/sh

# 启动红包获取程序
./receive_red_bag.py &

sleep 30s
echo '初始化完成...'

# 启动格子广告红包程序
./click_city_box.py &
echo '格子广告启动成功'

# 启动红包消费程序
./click_red_bag.py &
echo '红包消费启动成功'

echo '完成'