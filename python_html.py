# coding=utf-8
"""
python为我们提供了很多解析 html页面的库，其中常用的有：
bs4中的 BeautifulSoup，
lxml中的 etree（一个 xpath解析库）。
    BeautifulSoup类似 jQuery的选择器，通过 id、css选择器和标签来查找元素。
    xpath主要通过 html节点的嵌套关系来查找元素，和文件的路径有点像。
    
ref url:
https://www.jianshu.com/p/091c3aa0a73b

"""
# 导入 etree类
from lxml import etree
 
# 作为示例的 html文本
html = '''<div class="container">
                <div class="row">
                    <div class="col">
                        <div class="card">
                            <div class="card-content">
                                <a href="#123333" class="box">
                                    点击我
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>'''
 
#对 html文本进行处理 获得一个_Element对象
dom = etree.HTML(html)
 
#获取 a标签下的文本
a_text = dom.xpath('//div/div/div/div/div/a/text()')
 
print(a_text)