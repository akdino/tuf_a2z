arr=[-5,3,2,1,-3,-3,7,2,2]
def merge(arr):
    n=len(arr)
    if n==1:
        return arr
    m=len(arr)//2
    l=arr[:m]
    r=arr[m:]
    l,r=merge(l),merge(r)
    l_len,r_len=len(l),len(r)
    left,right=0,0
    new_arr=[0]*n
    i=0
    while left<l_len and right<r_len:
        if l[left]<r[right]:
            new_arr[i]=l[left]
            left+=1
        else:
            new_arr[i]=r[right]
            right+=1
        i+=1
    while left<l_len:
        new_arr[i]=l[left]
        left+=1
        i+=1
    while right<r_len:
        new_arr[i]=r[right]
        right+=1
        i+=1
    return new_arr
        
print(merge(arr))