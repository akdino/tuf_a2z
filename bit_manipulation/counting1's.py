def counting_1(n):
    dp=[0]*n+1
    for i in range(n+1):
        dp[i]=dp[i>>1]+(i&1)
    return dp

def missing_nums(n):
    r=0
    for i in range(len(n)):
        r=r^n[i]^i+1
    return r