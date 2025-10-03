def subarraySum(self, nums,k: int) -> int:
    d={0:1}
    presum=0
    final=0
    for i in nums:
        presum+=i
        if presum-k in d:
            final+=d[presum-k]
        if presum in d:
            d[presum]+=1
        else:
            d[presum]=1
        
    return final