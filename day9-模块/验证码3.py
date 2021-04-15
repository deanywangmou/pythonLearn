# coding=utf-8
import random
def get_code():
    ret=''
    for  i  in range(5):
        num=random.randint(0,9)
        alf=chr(random.randint(65,122))
        new=str(random.choice([num,alf]))
        ret+=new
    return  ret

print(get_code())
print(random.choice[1,2,3,4,5,6])