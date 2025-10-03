class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        hashmap={i:-1 for i in ["a","b","c"]}
        r=0
        final=0
        while r<len(s):
            hashmap[s[r]]=r
            if hashmap["a"]>=0 and hashmap["b"]>=0 and hashmap["c"]>=0:
                m=min(hashmap["a"],hashmap["b"],hashmap["c"])
                final+=m+1
            r+=1
        return final
    
'''
really good approach:
based on index 
aaabc
a=0 b=-1 c=-1 aaabc
a=1 b=-1 c=-1
a=2 b=-1 c=-1
a=2 b=3  c=-1
a=2 b=3  c=4(min=2)
so add 2 to final 
window of min substr is min(a,b,c) to max(a,b,c) ie from 2 to 4:abc


'''