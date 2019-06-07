# coding=utf-8
class BlackMedium:
    feture = 'Ugly'

    def __init__(self, name, addr):
        self.name = name
        self.addr = addr

    def sell_hourse(self):
        print('[%s]正在买房子，傻子才买呢' % self.name)

    def sell_hourse(self):
        print('[%s]正在租房子，傻子才租呢' % self.name)


b = BlackMedium('万科置业', '深圳片区')

print(hasattr(b, 'name'))  # True
print(hasattr(b, 'sell_hourse'))  # True

print(getattr(b, 'name'))  # 万科置业
print(getattr(b, 'addr'))  # 深圳片区
fun = getattr(b, 'sell_hourse')  # 如果没有这个值就报错，加默认参数则不报错
fun()  # [万科置业]正在租房子，傻子才租呢

# 设置值
# b.sb=True
setattr(b, 'sb', True)
print(b.__dict__)  # {'name': '万科置业', 'addr': '深圳片区', 'sb': True}

setattr(b, 'func1', lambda self: self.name + 'sb')
print(b.func1(b))  # 万科置业sb 

# 删除值
# del  b.sb
delattr(b, 'sb')
print(b.__dict__)  # {'name': '万科置业', 'addr': '深圳片区'}
