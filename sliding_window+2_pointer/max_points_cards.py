def maxScore( cardPoints, k: int) -> int:
    l_sum,r_sum=sum(cardPoints[:k]),0
    l,r=k-1,len(cardPoints)-1
    m=l_sum
    print(l,r)
    while l>=0 and r>=len(cardPoints)-k:
        print("yes")
        l_sum-=cardPoints[l]
        r_sum+=cardPoints[r]
        l-=1
        r-=1
        print(l,r)
        m=max(m,l_sum+r_sum)
    return m