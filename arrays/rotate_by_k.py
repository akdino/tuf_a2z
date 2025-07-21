'''
nums = [1,2,3,4,5,6,7], k = 3
Output: [4,5,6,7,1,2,3]

'''
def rotate_left(arr,k):
    k=k%len(arr)
    if k==0 or len(arr)==1:
        return arr
    temp=arr[:k]
    print(temp)
    print(temp,len(arr)-k-1,len(arr))
    for i in range(0, len(arr)-k):
        arr[i]=arr[i+k]
        print(arr[i])
    for i in range(len(arr)-k,len(arr)):
        arr[i]=temp[i-k-1]
        
    return arr
print(rotate_left([1,2,3,4,5,6,7],3))
'''
tc: O(k)+O(n-k)+O(k)=O(n+d)
'''

def otpimal(arr,k):
    n=len(arr)
    k=k%len(arr)
    arr[:]=arr[len(n)-k:]+arr[:len(n)-k]