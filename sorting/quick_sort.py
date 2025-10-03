arr=[-5,3,2,1,-3,-3,7,2,2]

def quick_sort(arr):
    if len(arr)<=1:
        return arr
    p=arr[-1]
    left=[x for x in arr[:-1] if x<=p]
    right=[x for x in arr[:-1] if x>p]
    l=quick_sort(left)
    r=quick_sort(right)
    return l+[p]+r

k=quick_sort(arr)
print(k)
if len(k)>2:
    print(k[-2])

