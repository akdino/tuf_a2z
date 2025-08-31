def ps(i,lst,arr):
    if i>=len(arr):
        print(lst)
        return
    lst.append(arr[i])
    ps(i+1,lst,arr)
    lst.pop()
    ps(i+1,lst,arr)

ps(0,[],[1,2,3 ])

