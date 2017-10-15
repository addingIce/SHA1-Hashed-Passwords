#coding = utf-8

import hashlib
import time
from itertools import *


t1 = ['=','0']
t2 = ['(','8']
t3 = ['%','5']
t4 = ['*','+']
t5 = ['w','W']
t6 = ['n','N']
t7 = ['i','I']
t8 = ['q','Q']

print time.strftime('%H:%M:%S',time.localtime(time.time()))
flag = 1
for keylist in product(t1,t2,t3,t4,t5,t6,t7,t8):        #t1--t8的笛卡尔积
    for t in list(permutations(keylist,8)):             #每个8个字符组合的全排列
        key = ''.join(t)
        Hash = hashlib.sha1()
        Hash.update(key)
        result = Hash.hexdigest()
        if result == '67ae1a64661ac8b4494666f58c4822408dd0a3e4':
            print key
            print time.strftime('%H:%M:%S',time.localtime(time.time()))
            flag = 0
            break
    if flag == 0:
        break
