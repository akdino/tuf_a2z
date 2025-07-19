def brute(arr):
    s=set(arr)
    l=list(s)
    for i in range(len(s)):
        arr[i]=l[i]
    return len(s)

'''
without sorting tc: O(n)
with sorting tc: O(nlogn)
'''