def pow(x,n):
    return x**n

def nthpower(m,n):
    high,low=m,1
    while low<=high:
        mid=(high+low)//2
        if pow(mid,n)==m:
            return mid
        elif pow(mid,n)<m:
            low=mid+1
        else:
            high=mid-1
