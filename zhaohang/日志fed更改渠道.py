# coding=utf-8
import os

with open(r'C:\Users\24368\Desktop\数据服务\laster_fed', 'r', encoding='utf8') as  f1, \
        open(r'C:\Users\24368\Desktop\数据服务\laster_fed1', 'w', encoding='utf8') as f4:
    r_list = f1.readlines()

    i = 0
    while i < len(r_list):
        if i < 10:
            new_str = r_list[i]
        else:
            new_str = r_list[i].replace("source:-", "source:false")
        print(new_str)
        f4.write(new_str)
        i += 1
