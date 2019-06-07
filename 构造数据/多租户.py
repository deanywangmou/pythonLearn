# coding=utf-8
import random

with open(r'C:\Users\24368\Desktop\数据服务\laster_gen', 'r', encoding='utf-8') as f1, \
        open(r'C:\Users\24368\Desktop\laster_gen', 'w', encoding='utf-8') as f2:
    r_list = f1.readlines()
    i = 0
    while i < len(r_list):
        randNum = random.randint(1, 2)
        print('>>>>>>>>>>>>>>>>>>>',randNum)
        if i == 0:
            new_str = r_list[i]
        elif randNum == 1:
            new_str = r_list[i].replace("is_private:0", "is_private:1")
        elif randNum == 2:
            new_str = r_list[i].replace("is_private:0", "is_private:2")

        # print(new_str)
        f2.write(new_str)
        i += 1
