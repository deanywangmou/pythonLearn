# coding=utf-8
import random

print(10 * random.random())
print(random.randint(1, 3))  # 1~3都可以取[1,3]
print(random.randrange(1, 3))  # 随机1，2，不可以取3[1,3)
print(random.choice([1, 2, '1212', 5]))  # 随机选出1个
print(random.sample([1, 2, '1212', 5], 3))  # 随机选出3个
print(random.uniform(1, 4))  # 取出1~4之间任意的浮点型

ret = [1, 4, 8, 9, 3, 2]
random.shuffle(ret)  # 将顺序打乱
print(ret)


