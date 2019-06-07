# coding=utf-8
class Foo:
    pass


f1 = Foo()
print(isinstance(f1, Foo))  # True


class Foo2(Foo):
    pass


print(issubclass(Foo2, Foo))  # True
