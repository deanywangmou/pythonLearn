import time
class FileHandle:
    def __init__(self,filename,mode='r',encoding='utf-8'):
        if 'b' in mode:
            self.file=open(filename,mode)
        else:
            self.file=open(filename,mode,encoding=encoding)
        self.filename=filename
        self.mode=mode
        self.encoding=encoding

    def write(self,line):
        if 'b' in self.mode:
            if not isinstance(line,bytes):
                raise TypeError('must be bytes')
        self.file.write(line)

    def __getattr__(self, item):
        return getattr(self.file,item)

    def __str__(self):
        if 'b' in self.mode:
            res="<_io.BufferedReader name='%s'>" %self.filename
        else:
            res="<_io.TextIOWrapper name='%s' mode='%s' encoding='%s'>" %(self.filename,self.mode,self.encoding)
        return res
f1=FileHandle('b.txt','wb')
# f1.write('你好啊啊啊啊啊') #自定制的write,不用在进行encode转成二进制去写了,简单,大气
f1.write('你好啊'.encode('utf-8'))
print(f1)
f1.close()


print(list(enumerate('deany')))