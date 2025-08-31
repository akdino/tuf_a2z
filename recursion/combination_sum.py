def combsum(ind,target,lst):
    if ind==len(arr):
        if target==0:print(lst)
        return
    if target>=arr[ind]:
        lst.append(arr[ind])
        combsum(ind,target-arr[ind],lst)
        lst.pop()
    combsum(ind+1,target,lst)

arr=[2,3,1,4,5,1,2,3]
#combsum(0,5,[])

n=len(arr)
def combsum2(ind,target,lst):
    if target==0:
        print(lst[:])
        return 
    for i in range(ind,n):
        if i>ind and arr[i]==arr[i-1]:continue
        if arr[i]>target:break
        lst.append(arr[i])
        combsum2(i+1,target-arr[i],lst)
        lst.pop()
combsum2(0,5,[])