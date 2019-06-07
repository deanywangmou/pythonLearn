#!/usr/bin/env python
# -*- coding:utf8 -*-

# filter函数
movie_people = ['sb_huang', 'sb_chen', 'deany', 'sb_wang']


def sb_start(m):  # lambda m:m.startswith('sb')
    return m.startswith('sb')


def sb_end(m):
    return m.endswith('sb')


def filter_test(func, array):
    ret = []
    for i in array:
        if not func(i):
            ret.append(i)
    return ret


print(filter_test(sb_start, movie_people))
print(filter_test(lambda n: n.startswith('sb'), movie_people))
print(list(filter(sb_start, movie_people)))
print(list(filter(lambda n: not n.startswith('sb'), movie_people)))
