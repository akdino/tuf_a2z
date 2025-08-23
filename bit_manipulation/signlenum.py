

def singlenum1(n):
    x=0
    for i in n:
        x=x^i
    return x

def singlenum2(n):
    pass

def singlenum3(n):
    x=0
    for i in n:
        x=x^i
    rightmost=x ^ (x&x-1)
    b1,b2=0,0
    for i in n:
        if rightmost&i:b1=b1^i
        else: b2=b2^i
    return [b1,b2]
