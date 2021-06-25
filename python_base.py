# coding=utf-8

# python中执行系统命令
# https://cloud.tencent.com/developer/article/1445388

# python的偏函数
# https://www.cnblogs.com/zhaopanpan/p/9397485.html


# 添加系统路径
'''
方式1
import sys
sys.path.append("/home/simon/Library")
方式2
vim ~/.bashrc
export PYTHONPATH=/home/simon/Library:$PYTHONPATH
方式3
import sys
print sys.path
找到site-packages路径，在路径下添加一个路径文件（以.pth为后缀），将模块文件所在目录写入路径文件中即可。
'''
