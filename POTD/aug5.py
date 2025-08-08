def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
    n=len(fruits)
    flag=[0]*n
    placed=0
    for i in range(n):
        for j in range(n):
            if fruits[i]<=baskets[j] and flag[j]==0:
                flag[j]=1
                placed+=1
                print(fruits[i],baskets[j])
                break
                
    return n-placed