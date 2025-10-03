def longestKSubstr( s, k):
    l,r=0,0
    max_len=0
    current=""
    while r<len(s):
        print(current)
        current+=s[r]
        
        if len(set(current))>k:
            current=current[1:]
            l+=1
        if len(set(current))==k:
            max_len=max(max_len,r-l+1)
        r+=1
    if max_len==0:
        return -1
    return max_len
print(longestKSubstr("aaaaaaa",2))

'''use hashmap instead'''
        
    