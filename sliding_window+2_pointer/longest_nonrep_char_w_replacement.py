def characterReplacement(self, s: str, k: int) -> int:
    hm=[0]*26
    l,r=0,0
    max_freq=0
    max_len=0
    while r<len(s):
        hm[ord(s[r])-65]+=1
        max_freq=max(max_freq,hm[ord(s[r])-65])
        while r-l+1 - max_freq>k:
            hm[ord(s[l])-65]-=1
            l+=1
            max_freq=max(hm)
        if r-l+1 - max_freq<=k:
            max_len=max(max_len,r-l+1)
        r+=1
    return max_len