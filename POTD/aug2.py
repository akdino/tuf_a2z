from collections import Counter
def minCost( basket1, basket2) -> int:
    
    c1=Counter(basket1)
    c2=Counter(basket2)
    m=min(min(basket1),min(basket2))

    s1,s2=[],[]
    cost=0
    

    for i in list(set(basket1)):
        total = c1[i] + c2[i]
        if total%2!=0:
            return -1
        if c1[i]>(c1[i]+c2[i])//2:
            k=c1[i]-(c1[i]+c2[i])//2
            s1.extend([i]*k)
    for i in list(set(basket2)):
        total = c1[i] + c2[i]
        if total%2!=0:
            return -1
        if c2[i]>(c1[i]+c2[i])//2:
            s2.extend([i]*(c2[i]-((c1[i]+c2[i])//2)))
    if s1==[]:
        return cost
    s1.sort()
    s2.sort(reverse=True)
    for i in range(len(s1)):
        cost+=min(min(s1[i],s2[i]),m*2)
    return cost