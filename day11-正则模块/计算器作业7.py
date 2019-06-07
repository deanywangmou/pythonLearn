# coding=utf-8
import re
s='1-2*((60+2*(-3-40.0/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'
ss=s.replace(" ","")
print(ss)
content=re.search('\(([\-\+\*\/]*\d+\.?\d*)+\)',ss).group() #(-3-40.0/5)
print(content)

print(re.search('(\d)+','123').group()) #group的作用是将所有组拼接到一起显示出来
print(re.findall('(\d)+','123')) #findall结果是组内的结果,且是最后一个组的结果