import math
def primes(n):
    k=[1]*(n+1)
    for i in range(2,n+2):
        for j in range(2*i,n+1,i):
            k[j]=0
    print("non",k)
    return k.count(1)-2

def optimal(n):
    k=[1]*(n+1)
    for i in range(2,int(math.sqrt(n))+1):
        for j in range(i*i,n+1,i):
            k[j]=0
    print(k)
    return k.count(1)-2


k=optimal(30)
n=primes(30)
print(k,n)