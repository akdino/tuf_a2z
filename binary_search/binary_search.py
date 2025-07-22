def iterative(arr,target):
    n=len(arr)
    low,high=0,n-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1

arr=[1,2,3,4,5,6,7,8,9]
print("5: ",iterative(arr,5)," 8:",iterative(arr,8)," 10: ",iterative(arr,10))

def bs(arr,low,high,target):
    if low>high:
        return -1
    mid=(low+high)//2
    if arr[mid]==target:
        return mid
    elif arr[mid]<target:
        return bs(arr,mid+1,high,target)
    else:
        return bs(arr,low,high-1,target)
    
print("5: ",bs(arr,0,8,5)," 8:",bs(arr,0,8,8)," 10: ",bs(arr,0,8,10))
