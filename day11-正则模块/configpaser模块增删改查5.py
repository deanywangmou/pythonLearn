# coding=utf-8
import configparser

config = configparser.ConfigParser()

# --------------------------------查
print(config.sections())  # []
config.read('example.ini')
print(config.sections())  # ['bitbucket.org', 'topsecret.server.com']
print('bitbucket.org' in config)  # True

print(config['bitbucket.org']['user'])  # hg

for i in config['topsecret.server.com']:
    print(i)  # host port forwardx11 serveraliveinterval compression compressionlevel
    # 注意：默认default中的所有键都会被打印出来

print(config.options(
    'topsecret.server.com'))  # ['host port', 'forwardx11', 'serveraliveinterval', 'compression', 'compressionlevel']

print(config.items(
    'topsecret.server.com'))  # [('serveraliveinterval', '45'), ('compression', 'yes'), ('compressionlevel', '9'),
# ('forwardx11', 'no'), ('host port', '50022')]

print(config.get('topsecret.server.com', 'compression'))  # yes

# -----------------------------------------------------------删改查
config.add_section('add')
config.set('add', 'k1', '1111')
config['add']['k2']='k222'

# config.remove_section('bitbucket.org')#删除块
config.remove_option('bitbucket.org', 'user')  # 删除块下面的某一键值对
#
config.write(open('newconfig', 'w'))
