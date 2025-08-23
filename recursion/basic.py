def prt(n):
    if n==0:return 
    print("anagha")
    prt(n-1)

def prnt(i,n):
    if i>n:return 
    print("anagha")
    prnt(i+1,n)

def num(n):
    if 0>=n:return 
    print(n)
    num(n-1)
'''
f(4)->f(3)->f(2)->f(1)->f(0)
4 3 2 1
'''

def num_backtrack(n):
    if 0>=n:return 
    num_backtrack(n-1)
    print(n)
'''
f(4)->f(3)->f(2)->f(1)->f(0)
f(0) returns -> f(1) prints(1)->f(2) prints 2->f(3) prints(3)->f(4)prints(4)

'''

def rev_backtrack(i,n):
    if i>n:return 
    rev_backtrack(i+1,n)
    print(i)

def param_sum(i,sum):
    if i<1:
        print(sum)
        return
    
    param_sum(i-1,sum+i)

def func_sum(n):
    if n==0:return 0
    return n+func_sum(n-1)


def fact(n):
    if n==1:return 1
    return n* fact(n-1)
k=fact(4)


def revarr(l,r,a):
    if l>=r:return 
    a[l],a[r]=a[r],a[l]
    revarr(l+1,r-1,a)


def palindrome(i,s):
    if i>len(s)//2:return True
    if s[i]!=s[len(s)-i-1]:return False
    return palindrome(i+1,s)
print(palindrome(0,"madam"))