def reorderedPowerOf2( n: int) -> bool:
    powers=[]
    for i in range(30):
        powers.append(2**i)
    if n in powers:
        return True
    l=list(str(n))
    silimar_length=len(l)
    check=[]
    
    l.sort()
    for i in powers:
        k=list(str(i))
        if len(k)==silimar_length:
            k.sort()
            if k==l:
                return True
    return False
