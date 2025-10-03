def lengthOfLongestSubstring(self, s: str) -> int:
    l,r=0,0
    max_len=0
    current=""
    while r<len(s):
        current+=s[r]
        if len(set(current))==len(current):
            max_len=max(max_len,r-l+1)
        while len(set(current))<len(current):
            current=current[1:]
            l+=1
        r+=1
    return max_len

def longnonreap(self, s: str) -> int:
    l=0
    max_len=0
    seen=set()
    for r in range(len(s)):
        while s[r] in seen:
            seen.remove(s[l])
            l+=1
        seen.add(s[r])
        max_len=max(max_len,r-l+1)
    return max_len