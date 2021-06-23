# coding=utf-8
"""
ElementTree是Python常用的处理XML文件的类。本文将介绍使用ElementTree解析、查找、修改XML的方法

XML的格式样例及其说明：
<?xml version="1.0" encoding="utf-8" ?>
    <sitemapindex>
        <sitemap>
            <loc>http://www.zhaopin.com/url1.xml</loc>
            <lastmod>2010-04-26</lastmod>
        </sitemap>
    </sitemapindex>
 
Tag： 使用<和>包围的部分，如<rank>成为start-tag，</rank>是end-tags；
Element：被Tag包围的部分，如<rank>68</rank>，可以认为是一个节点，它可以有子节点；
Attribute：在Tag中可能存在的name/value对，如<country name="Liechtenstein">中的name="Liechtenstein"，一般表示属性。

参考
https://www.jianshu.com/p/cf6fa10045a6
"""
import codecs
 
# ElementTree是Python常用的处理XML文件的类。本文将介绍使用ElementTree解析、查找、修改XML的方法
import xml.etree.cElementTree as ET
 
 
class XmlOp(object):
    """xml处理
    """
    def __init__(self, xml_path=None, create_tree=False):
        if xml_path:
            self.tree = self.read_xml(xml_path)
        elif create_tree:
            elem = self.create_node("root")
            self.tree = ET.ElementTree(elem)
        self.root = self.tree.getroot()
                     
    def create_node(self, tag, property_map=None, content=None):
        """新造一个节点
        tag:节点标签
        property_map:属性及属性值map
        content: 节点闭合标签里的文本内容
        return 新节点"""
        element = ET.Element(tag)
        if property_map:
            for k, v in property_map.items():
                element.set(k, v)
        if content:
            element.text = content
        return element
 
    def read_xml(self, in_path):
        """从文件加载xml
        """
        tree = ET.ElementTree(file=in_path)
        return tree
                 
    def read_xml_string(self, sample_as_string):
        """从字符传读入xml
        """
        root = ET.fromstring(sample_as_string)
         
    def write_xml(self, out_path):
        """将xml文件写出
        tree: xml树
        out_path: 写出路径"""
        self.tree.write(out_path, encoding="utf-8", xml_declaration=True)
         
    def if_match(self, node, kv_map):
        """判断某个节点是否包含所有传入参数属性
        node: 节点
        kv_map: 属性及属性值组成的map"""
        for key in kv_map:
            if node.get(key) != kv_map.get(key):
                return False
        return True
     
    def set_property(self, node, k, v):
        """[summary]
        """
        node.set(k, v)
     
    def find_nodes(self, xpath):
        """查找某个路径匹配的所有节点
        tree: xml树
        xpath: 节点路径
         
        xml库中的Elment对象支持以xpath的方式查找节点
        xpath 语法
        [@]：选择具有某个属性的节点
        //div[@classs], //a[@x]：选择具有 class属性的 div节点、选择具有 x属性的 a节点
        //div[@class="container"]：选择具有 class属性的值为 container的 div节点
        //a[contains(text(), "点")]：选择文本内容里含有 “点” 的 a标签，比如上面例子中的两个 a标签
        //a[contains(@id, "abc")]：选择 id属性里有 abc的 a标签
         
        / 路径层级关系
        a / b ：‘/’在 xpath里表示层级关系，左边的 a是父节点，右边的 b是子节点，这里的 b是 a的直接子节点
        a // b：两个 / 表示选择所有 a节点下的 b节点（可以是直接子节点，也可以不是），在上面的例子中我们要选择 a标签是这样写的
 
        """
        return self.tree.findall(xpath)
     
    def edit_node_text(self, node, text):
        """修改节点text
        """
        node.text = text
     
    def insert_node(self, node1, node2):
        """插入节点
        """
        node1.append(node2)
 
    def del_node_attribute(self, node, key):
        """删除节点
        """
        del node.attrib[key]