from gmssl import sm3
import time 
from random import *
dep = 4

def SM3_Rho():
    start = sm3.sm3_hash([randint(0, 2 ** 32)])
    x = strtint_l(start)[:]
    y = strtint_l(start)[:]
    l = 0
    while(1):
        x = sm3.sm3_hash(x)
        tempx = x[:]
        x = strtint_l(x)[0:dep]
        
        y = sm3.sm3_hash(y)
        y = strtint_l(y)[0:dep]
        y = sm3.sm3_hash(y)
        
        tempy = y[:]
        y = strtint_l(y)[0:dep]
        l = l + 1

        if (tempx[0:dep] == tempy[0:dep]):
            break

    print("循环长度: ",l)
    x = strtint_l(start)
    y = strtint_l(start)
    for i in range(l):
        x = sm3.sm3_hash(x)
        x = strtint_l(x)
    print(x)
    while(1):
        x = sm3.sm3_hash(x)
        y = sm3.sm3_hash(y)
        if(x[0:dep] == y[0:dep]):
            return [tempx, tempy]
        x = strtint_l(x)
        tempx = x[:]
        y = strtint_l(y)
        tempy = y[:]

    
def strtint_l(s):
    return [int(s[i],16) for i in range(0,64)]

start = time.time()
mx, my = SM3_Rho()
print(" :\nmx : {}\nmy : {}".format(mx, my))
hashx = sm3.sm3_hash(mx)
hashy = sm3.sm3_hash(my)
print("hash(mx) : ", hashx)
print("hash(my) : ", hashy)
if (hashx[0:dep] == hashy[0:dep]):
    print("success")
end = time.time()
print("用时: {:.5f}s".format(end-start))
