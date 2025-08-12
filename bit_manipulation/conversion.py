def tobin(n):
    if n==0:return 0
    k=""
    while n>=1:
        if n%2==0:k+="0"
        else:k+="1"
        n=n//2
    return int(k[::-1])

def todec(n):
    k=0
    n=n[::-1]
    print(n)
    k=[int(n[i])*2**i for i in range(len(n))]
    return sum(k)


print(todec("101010"))
print(todec("10"))
print(int("10",2))

'''
functions to use:
binary to decimal => int("10010",2)
decimal to binary => bin(2)[2:] if n!=0
'''