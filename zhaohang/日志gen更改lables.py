# coding=utf-8
import os

with open(r'C:\Users\24368\Desktop\gen', 'r', encoding='utf8') as  f1, \
        open(r'C:\Users\24368\Desktop\gen1', 'w', encoding='utf8') as f2:
    r_list = f1.readlines()

    i = 0
    while i < len(r_list):
        if i % 3==0:
            new_str = r_list[i]
        elif i % 3 == 1:
            new_str = r_list[i].replace("tags:WeiXin", "tags:ATP")
        else:
            new_str = r_list[i].replace("tags:WeiXin", "tags:QQ")

        print(new_str)
        f2.write(new_str)
        i += 1
