
def mySqrt( x:int) -> int:
    if x==0:
        return 0
    if x==1:
        return 1
    ans=1
    high,low=x,1
    while low<=high:
        mid=(low+high)//2
        if mid**2<=x:
            ans=mid
            low=mid+1
        elif mid**2>x:
            high=mid-1
    return ans
            