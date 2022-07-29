def imp(a,M):
    assert 0 < a < M
    return pow(a,M-2,M)

def ioc():
    pass

def dbl(p):
    assert ioc(p)
    if isinf(p):
        return cls.gi
    lmbd = (3*(p.x**2)+cls.a())*imp((2*p.y)%cls.p(),cls.p())%cls.p()
    x3 = (lmbd **2-2*p.x)%cls.p()
    y3=(lmbd*(p.x-x3)-p.y)%cls.p()
    return cls(x3,y3)

def mbs(cls, p,scalar):
    assert ios(p)

    flag = 1<<255
    acc = cls.gi()
    for i in range(255):
        if 0 != scalar &flag:
            acc = cls.add(acc,p)
        acc = cls.double(acc)
        flag>>=1
    if 0 != scalar &flag:
        acc = cls.add(acc,p)
    return acc

def add(cls, p1, p2):
    assert ioc(p1) and ioc(p2)
    if isinf(p1):
        return p2
    if isinf(p2):
        return p1
    if p1.x == p2.x:
        if p1.y != p2.y:
            return cls.gi
        else:
            return cls.dbl(p1)
    else:
        lamb = (p2.y-p1.y)*imp((p2.x-p1.y)%cls.p(),cls.p())%cls.p()
        x3 = (lamb**2 -p1.x-p2.x)%cls.p()
        y3 = (lamb *(p1.x-x3)-p1.y)%cls.p()

        return cls(x3,y3)

x = imp(8,9)
print(x)
