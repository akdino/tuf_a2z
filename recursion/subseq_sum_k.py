
target=2

def sub(i,lst,s,arr):
    if i==len(arr):
        if s==target:print(lst)
        return 
    lst.append(arr[i])
    s+=arr[i]
    sub(i+1,lst,s,arr)
    lst.pop()
    s-=arr[i]
    sub(i+1,lst,s,arr)

#sub(0,[],0,[1,2,1])


def sub_cond(i,lst,s,arr):
    if i==len(arr):
        if s==target:
            print(lst)
            return True
        else: return False
    lst.append(arr[i])
    s+=arr[i]
    if (sub_cond(i+1,lst,s,arr)) == True: 
        return True
    lst.pop()
    s-=arr[i]
    if (sub_cond(i+1,lst,s,arr)) ==True: 
        return True
    return False

target=2

#sub_cond(0,[],0,[1,2,1])

'''
                  ______[]______
                 /              \
                /                \
               /                  \
              /                    \
             /                      \
            [1]                      []      
         /       \                  /   \
     [1,2]         [1]            [2]      []  
    /     \       /   \          /  \     /  \
  [1,2,1] [1,2]  [1,1] [1]    [2,1] [2]  [1] []
'''


def count_sub(i,lst,s,arr):
    if i == len(arr):
        if s==target:return 1
        else:return 0
    lst.append(arr[i])
    s+=arr[i]
    l=count_sub(i+1,lst,s,arr)
    lst.pop()
    s-=arr[i]
    r=count_sub(i+1,lst,s,arr)
    return l+r
target=2
res=count_sub(0,[],0,[1,2,1])
print(res) 