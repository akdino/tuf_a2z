def numberOfSubarrays(self, nums, k: int) -> int:
    def atmost(k):
        l,r,s,count=0,0,0,0
        if k<0:
            return 0
        while r<len(nums):
            s+=nums[r]&1
            while s>k:
                s-=nums[l]&1
                l+=1
            count+=r-l+1
            r+=1
        return count
    return atmost(k)-atmost(k-1)