def brute_second_largest(arr):
    arr.sort()
    largest=arr[-1]
    for i in range(len(arr)-2, 0, -1):
        if arr[i] != largest:
            return arr[i]
'''
tc: O(nlogn+n)=> O(nlogn)
'''
    
def better_second_largest(arr):
    largest=float('-inf')
    second_largest=float('-inf')
    for i in range(len(arr)):
        if arr[i]>largest:
            largest=arr[i]
    for i in range(len(arr)):
        if arr[i]!=largest and arr[i]>second_largest:
            second_largest=arr[i]
    return second_largest

'''
tc: O(2n)=>O(n)
'''

def optimal_second_largest(arr):
    largest=arr[0]
    second_largest=float('-inf')
    for i in range(len(arr)):
        if arr[i]>largest:
            second_largest=largest

            largest=arr[i]
        elif arr[i]!=largest and arr[i]>second_largest:
            second_largest=arr[i]
        
    return second_largest

'''
tc: O(n)
'''


arr=[1,2,4,7,7,5]
print(optimal_second_largest(arr))
