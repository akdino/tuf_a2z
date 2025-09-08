def subset(ind,lst,sum):
    if ind==len(arr):
        print(sum,lst)
        return 
    lst.append(arr[ind])
    sum+=arr[ind]
    subset(ind+1,lst,sum)
    lst.pop()
    sum-=arr[ind]
    subset(ind+1,lst,sum)
arr=[1,2,3,4]
subset(0,[],0)