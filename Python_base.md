#### python添加系统路径
- 方式1  
import sys  
sys.path.append("/home/simon/Library")
- 方式2  
vim ~/.bashrc  
export PYTHONPATH=/home/simon/Library:$PYTHONPATH
- 方式3(推荐)  
import sys
print sys.path
找到site-packages路径，在路径下添加一个路径文件（以.pth为后缀），将模块文件所在目录写入路径文件中即可。
![py_sys_path.png](https://github.com/rhh2019/work_learn/blob/main/pic/py_sys_path.png)
![py_sys_path.png](https://github.com/rhh2019/work_learn/blob/main/pic/duola.jpg)

https://sm.ms/
