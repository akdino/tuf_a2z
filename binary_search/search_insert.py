def insert(nums,target):
    n=len(nums)
    ans=n
    if target<=nums[0]:
        return 0
    high,low = n-1,0
    while low<=high:
        mid=(low+high)//2
        if nums[mid]>=target:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
