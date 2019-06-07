# coding=utf-8
class Open:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('执行entrt')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('执行exit')
        print(exc_type)
        print(exc_val)
        print(exc_tb)



with  Open('a.txt') as  f:
    print(f)
    print(f.name)
