# coding=utf-8


def dog(name, sex, type):
    def eat(dog):
        print('[%s]吃骨头' % dog['name'])

    def action(dog):
        print('狗的职责是[%s]' % dog['type'])

    def init(name, sex, type):
        dog1 = {
            'name': name,
            'sex': sex,
            'type': type,
            'eat': eat,
            'action': action
        }
        return dog1

    return init(name, sex, type)
    # dog1 = {
    #     'name': name,
    #     'sex': sex,
    #     'type': type,
    #     'eat': eat,
    #     'action': action
    # }
    #
    # return dog1


d1 = dog('旺财', '母', '看门')
print(type(d1))
print(d1)
d1['action'](d1)
