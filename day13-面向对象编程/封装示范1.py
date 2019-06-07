# coding=utf-8

class Room:
    def __init__(self, name, owner, width, length, high):
        self.name = name
        self.owner = owner
        self.__width = width
        self.__length = length
        self.__high = high

    @property
    def tell_area(self):
        return self.__width * self.__length


r = Room('卫生间', '王某', 15, 15, 4)
print(r.tell_area)
