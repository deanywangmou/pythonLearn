# coding=utf-8
def fetch(data):
    print('这是查询功能')
    print('\033[1;44m用户数据是\033[0m%s' % data)

    backend_data = 'backend %s' % data

    with open('address.config', 'r', encoding='utf8') as read_f:
        tag = False
        ret = []
        for read_line in read_f:
            if read_line.strip() == backend_data:
                tag = True
                continue

            if tag and read_line.startswith('backend'):
                break

            if tag:
                print('\033[1;45m%s\033[0m' % read_line, end='')
                ret.append(read_line)

    return ret


def add():
    pass


# ['server  100.123.112.33  weight 20  max  50\n', 'server  31.33.76.1  weight 12  max  7\n',
# 'server  21.1.46.7  weight 23  max  56\n', 'server  56.5.86.55  weight 56  max  8\n', '\n']
def change(data):
    print('这是修改功能')
    print('用户输入的数据是%s' % data)
    backend=data[0]['backend']
    res=fetch(backend)
    print('来自change函数--->',res)


def delete():
    pass


if __name__ == '__main__':
    msg = '''
    1:查询
    2:添加
    3:修改
    4:删除
    5:退出
    '''
    msg_dic = {
        '1': fetch,
        '2': add,
        '3': change,
        '4': delete,
        '5': exit,
    }

    while True:
        print(msg)
        choice = input('请输入你的数据选项：').strip()
        if not choice: continue
        if choice == '5': break

        data = input('请输入你的数据').strip()
        if choice != '1':
            data = eval(data)

        res = msg_dic[choice](data)
        print(res)


    print(__name__)