def totalFruit( fruits) -> int:
    s=dict()
    l,r=0,0
    max_len=0
    while r<len(fruits):
        if fruits[r] not in s:
            s[fruits[r]]=1
        else:
            s[fruits[r]]+=1
        while len(s)>2:
            if s[fruits[l]]>0:
                s[fruits[l]]-=1
            if s[fruits[l]] == 0:
                del s[fruits[l]]
            l+=1
        max_len=max(max_len,r-l+1)
        r+=1
    return max_len
