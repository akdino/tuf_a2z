def findMin( nums) -> int:
    n=len(nums)
    m=float('inf')
    high,low=n-1,0
    while low<=high:
        mid=(low+high)//2
        if nums[low]<=nums[mid]:
            m=min(m,nums[low])
            low=mid+1
        else:
            m=min(m,nums[mid])
            high=mid-1
    return m


'''
arr=[4 5 6 7 0 1 2]
2 halves [4 5 6 7],[7 0 1 2]
sorted : arr[low]<arr[mid] ie the smallest: arr[low] ie 4
not sorted half : [0 1 2] => min:0
number of times array of size n is rotated is index of min
'''