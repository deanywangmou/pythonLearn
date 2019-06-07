def fun():
    print('11111')
    print('2222222---------')
    yield 1
    print('333333333333')
    print('44444--------')
    yield 2
    print('5555')
    print('666------------')
    yield 3
    print('777------')
    print('888')


f = fun()
s1 = f.__next__()
print(s1)
s2 = f.__next__()
print(s2)
s3 = f.__next__()
print(s3)

name = 'deany'


def show():
    print(id(name))


print(id(name))
show()

print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')


def tt():
    for i in range(5):
        yield i


t = tt()
t1 = (j for j in t)
print(list(t1))
