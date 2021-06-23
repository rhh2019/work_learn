#! /bin/sh
:<<EOF
单引号字符串的限制：
    单引号里的任何字符都会原样输出，单引号字符串中的变量是无效的；
    单引号字串中不能出现单独一个的单引号（对单引号使用转义符后也不行），但可成对出现，作为字符串拼接使用。

双引号的优点：
    双引号里可以有变量
    双引号里可以出现转义字符
EOF

your_name="runoob"
# 使用双引号拼接
greeting="hello, "$your_name" !"
greeting_1="hello, ${your_name} !"
echo $greeting  $greeting_1

# 使用单引号拼接
greeting_2='hello, '$your_name' !' # 单引号成对出现，作为字符串拼接使用
greeting_3='hello, ${your_name} !'
echo $greeting_2  $greeting_3