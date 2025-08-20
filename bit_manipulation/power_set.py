def powerset(n,nums):
    final=[]
    for i in range(1<<n):
        l=[]
        for j in range(n):
            if (1<<j)&i:
                l.append(nums[i])
        final.append(l)
    return final
