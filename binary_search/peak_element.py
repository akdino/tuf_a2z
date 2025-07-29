
def peakelement(nums):
    n=len(nums)
    if len(nums)==1:
        return 0
    if nums[0]>nums[1]:
        return 0
    if nums[n-1]>nums[n-2]:
        return n-1
    high,low=n-2,1
    while low<=high:
        mid=(low+high)//2
        if nums[mid-1]<nums[mid]>nums[mid+1]:
            return mid
        elif nums[mid-1]<nums[mid]:
            low=mid+1
        else:
            high=mid-1


'''
draw mountain diagram for analysis
'''