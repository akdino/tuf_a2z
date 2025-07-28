def search_in_rotated_1(arr,target):
        high,low=n-1,0
        while low<=high:
            mid=(high+low)//2
            if arr[mid]==target:
                return mid
            if arr[mid]>=arr[low]:
                if arr[low]<=target and arr[mid]>=target:
                    high=mid-1
                else:
                    low=mid+1
            elif arr[mid]<=arr[high]:
                if arr[mid]<=target and arr[high]>=target:
                    low=mid+1
                else:
                    high=mid-1
        return -1

def search_in_rotated_2(arr,target):
    pass