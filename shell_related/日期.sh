#! /bin/bash

# 先把日期处理成纯数字的格式
start=`date -d "2016-01-01" +%Y%m%d`
end=`date -d "2016-03-01" +%Y%m%d`

# 日期加1和减1
today="20210531"
tomorrow=`date -d "1 day ${today}" +%Y-%m-%d`	# 日期加1
yestoday=`date -d "-1 day ${today}" +%Y-%m-%d`	# 日期减1
echo ${yestoday}, ${today}, ${tomorrow}

# YESTERDAY
# DATE=$(date +%Y%m%d -d "1 day ago $DATE")