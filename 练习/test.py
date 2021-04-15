import re
class Person(object):
    static_var = 10
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def set_name(self,name):
        self.name = name
    @classmethod
    def set_staic_var(cls,var):
        Person.static_var = var
    def get_info(self):
        return "name: %s,age: %s" %(self.name,self.age)
    '''静态方法只能访问类变量，不能访问实例变量'''
    @staticmethod
    def get_class_var():
        return "calss var: %s" %Person.static_var
p = Person("zhangsan",18)
print(Person.get_class_var())
print(p.get_info())
p.set_name("lisi")
print(p.get_info())
p.set_staic_var(20)
print(p.get_info())
print(Person.get_class_var())



print(re.search(r"\d{5}","1234aadd2222223333").group())
print(re.findall(r"\d{5}","1234aadd22222rrr23333"))
print(re.match(r"\d{5}","1234aadd22222rrr23333"))
'''取最后一个字母'''
print(re.search(r"[A-Za-z]$","ab12cd").group())

'''找出一个字符串中的所有数字'''
pattern = re.compile(r"\d+")
print(pattern.findall("a1cd33dd99kddd"))

pattern1 = re.compile(r"\d")
print(pattern1.findall("a1cd33dd99kddd"))


s = "abc123"
print(re.match(r"^[A-Za-z]+",s).group())
print(re.search(r"^[A-Za-z]+",s).group())
print(re.match(r"\d{5}","12345aadd22222rrr23333").group())
