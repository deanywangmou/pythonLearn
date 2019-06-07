# coding=utf-8
import xml.etree.ElementTree as ET

tree = ET.parse("xml_file")
root = tree.getroot()
print('------',root)
print(root.tag)

# 遍历xml文档
for child in root:
    print(child.tag)
    print(child.attrib)
    print('text----->',child.text)
#     print('========>', child.tag, child.attrib, child.attrib['name'])
    for i in child:
        print(i.tag)
        print(i.attrib)
        print(i.text)
print('------------------------------')
#         print(i.tag, i.attrib, i.text)
#
# 只遍历year 节点
for node in root.iter('year'):
    print(node.tag, node.text)
# # ---------------------------------------
#
# import xml.etree.ElementTree as ET
#
# tree = ET.parse("xml文件")
# root = tree.getroot()
#
# 修改
for node in root.iter('year'):
    new_year = int(node.text) + 1
    node.text = str(new_year)
    node.set('updated', 'yes')
    node.set('version', '1.0')
    tree.write('abc.xml')

# 删除node
for country in root.findall('country'):
    rank = int(country.find('rank').text)
    if rank > 50:
        root.remove(country)

tree.write('output.xml')


# # 在country内添加（append）节点year2
import xml.etree.ElementTree as ET

tree = ET.parse("a.xml")
root = tree.getroot()
for country in root.findall('country'):
    for year in country.findall('year'):
        if int(year.text) > 2000:
            year2 = ET.Element('year2')
            year2.text = '新年'
            year2.attrib = {'update': 'yes'}
            country.append(year2)  # 往country节点下添加子节点

tree.write('a.xml.swap')