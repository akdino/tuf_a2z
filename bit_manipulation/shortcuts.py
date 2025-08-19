#1.xor shortcut to swap numbers
def swap(a,b):
    a=a^b
    b=a^b
    a=a^b
'''
a^a=0
a^0=a
'''

#2 to chech if set bits are 1
def checkbit(n,bit):
    return (n&(1<<bit))!=0
'''
given 13= '1101' and bit=1,2
1101
0010
----
0000

1101
0100
----
0001
'''

#3.set ith bit to 1
def setbit(n,bit):
    return n|(1<<bit)

#4.clear ith bit
def clearbit(n,bit):
    return n&(~(1<<bit))

#5.Toggle ith bit
def toggle(n,bit):
    return n^(1<<bit)

#6.clear rightmost bit
def clear_rightmost_bit(n):
    return n&(n-1)

#7.clear leftmost bit
def clear_leftmost_bit(n):
    return n&(~(n-1))

'''
n=5=101
n-1=4=100
n&n-1=0=000
'''
#power of 2
def check_power_of_2(n):
    return (n&(n-1))==0
'''
1000
0111
----
0000
'''

#8.popcount
def count_1s(n):
    count=0
    while n:
        count+=n&1
        n=n>>1
    return count
'''
1010
1101
1010
0000
count=2+3+2+0=7
'''