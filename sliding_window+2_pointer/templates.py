from collections import defaultdict
def constant_window(k,arr):
    l,r=0,k-1
    s=sum(arr[:k])
    m=s
    while r<len(arr)-1:
        l+=1
        s-=arr[l]
        r+=1
        s+=arr[r]
        m=max(s,m)
    return m
print(constant_window(4,[-1,2,3,3,4,5,-1]))

'''
for i in range(k,len(arr)):
    s+=arr[i]-arr[i-k]
    m=max(s,m)
'''

def variable_window(arr,k):
    l,r,s=0,0,0
    m_l=0
    while r<len(arr):
        s+=arr[r]
        if s<=k:
            m_l=max(m_l,r-l+1)
        while s>=k:
            s-=s[l]
            l+=1
        r+=1

def subarraysWithKDistinct(nums, k) -> int:
        def atMostK(k):
            count = 0
            l, r = 0, 0
            map = defaultdict(int)
            for r in range(len(nums)):
                map[nums[r]] += 1
                while len(map) > k:
                    map[nums[l]] -= 1
                    if map[nums[l]] == 0:
                        del map[nums[l]]
                    l += 1
                count += (r - l + 1)
            return count
        return atMostK(k) - atMostK(k - 1)

    