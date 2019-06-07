# coding=utf-8
import pickle


class Base:
    def save(self):
        with  open('school.db', 'wb') as  f:
            pickle.dump(self, f)
            # pickle.dumps(f.read)

class school(Base):
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr


class Course(Base):
    def __init__(self, name, price, period, school):
        self.name = name
        self.price = price
        self.period = period
        self.school = school


school_obj = pickle.load(open('school.db', 'rb'))
# f=open('school.db', 'rb')
# school_obj = pickle.loads(f.read())
print(school_obj.name, school_obj.addr)

# s1=school('老男孩','北京')
# s1.save()
