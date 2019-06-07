# coding=utf-8
class Fib:
    def __init__(self):
        self.a = 1
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.a > 1000:
            raise StopIteration('执行终止')
        self.a, self.b = self.b, self.a + self.b
        return self.a


f = Fib()
print(f.__next__())
print(f.__next__())
print(f.__next__())

print('>>>>>>>>>>>>>>>')
for i in f:
    print(i)
