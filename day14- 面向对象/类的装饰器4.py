# coding=utf-8

def typed(**kwargs):
    def deco(obj):
        # print(kwargs)
        for key, val in kwargs.items():
            setattr(obj, key, val)
        return obj

    return deco


@typed(x=1, y=2)  # 1.运行typed(x=1, y=2)得到deco   2.在运行@deco>>>deco=deco(Foo)
class Foo():
    pass


print(Foo.__dict__)



@typed(name='deany')  # 1.运行typed(name='deany')得到deco   2.在运行@deco>>>deco=deco(Bar)
class Bar():
    pass


print(Bar.__dict__)
