def leftroatate(arr):
    if len(arr) == 1:
        return arr
    temp=arr[0]
    for i in range(1,len(arr)):
        arr[i-1]=arr[i]
    arr[-1]=temp
    return arr

def rightroatate(arr):
    if len(arr) == 1:
        return arr
    temp=arr[-1]
    for i in range(len(arr)-1,0,-1):
        print(arr[i])
        arr[i]=arr[i-1]
    arr[0]=temp
    return arr

arr=[1,2,3,4,5]
print(rightroatate(arr))
arr=[1,2,3,4,5]
print(leftroatate(arr))
'''
for left rotate => [1,2,3,4,5]->[2,3,4,5,1] 
right roateate=> [5,1,2,3,4]
'''
