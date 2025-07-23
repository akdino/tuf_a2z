def lower_bound(arr,x):
    n=len(arr)
    ans=n
    high,low=n-1,0
    while low <= high:
        mid=(high+low)//2
        if arr[mid]>=x:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans

def upper_bound(arr,x):
    n=len(arr)
    ans=n
    high,low=n-1,0
    while low <= high:
        mid=(high+low)//2
        if arr[mid]>x:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans


