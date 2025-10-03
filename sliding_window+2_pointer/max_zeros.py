def longestOnes( nums, k: int) -> int:
    l,r=0,0
    z=0
    max_len=0
    while r<len(nums):
        if nums[r]==0:
            z+=1
        while z>k:
            if nums[l]==0:
                z-=1
            l+=1
        if z<=k:
            max_len=max(max_len,r-l+1)
        r+=1
    return max_len
