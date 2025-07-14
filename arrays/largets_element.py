def largest_element(arr):
    largest=float('-inf')
    for i in arr:
        if i>largest:
            largest=i
    return largest
arr=[13,46,24,52,20,9]
print(largest_element(arr))
''' 
brute force=> sorting tc: O(nlogn)
looping=> tc: O(n)
'''