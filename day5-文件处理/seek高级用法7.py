f = open('日志文件', 'rb')
for i in f:
    offs = -10
    while True:
        f.seek(offs, 2)
        data = f.readlines()
        if len(data) > 1:
            print('最后一行的结果是%s' % (data[-1].decode('utf8')))
            break
        offs *= 2
