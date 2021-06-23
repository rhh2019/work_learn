#! /bin/bash

# 打印起始和结束日期
start='2016-01-01'
end='2016-01-03'
# 左右条件一定要用""引起来，'不行
while [ "${start}" != "${end}" ]
do
  echo ${start}
  start=`date -d "1 day ${start}" +%Y-%m-%d`	# 日期自增
done