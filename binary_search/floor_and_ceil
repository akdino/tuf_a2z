def searchRange(nums,target):
        flag=-1
        n=len(nums)
        high,low=n-1,0
        while low<=high:
            mid=(high+low)//2
            if nums[mid]==target:
                flag=1
                while nums[high]!=target:
                    high-=1
                    
                while nums[low]!=target:
                    low+=1
                break
    
            if nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        
        if flag==-1:
            return [-1,-1]
        else:
            return [low,high]
