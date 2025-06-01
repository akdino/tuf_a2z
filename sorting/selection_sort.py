def selection_sort(arr):
    for i in range(len(arr)-1):
        min_index=i
        for j in range(i,len(arr)):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[min_index], arr[i]=arr[i], arr[min_index]
    return arr

arr=[13,46,24,52,20,9]
print(selection_sort(arr)) 