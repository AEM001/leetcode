class Solution:
    def mergeSort(self, nums: [int]) -> [int]:
        n=len(nums)
        self.gsort(nums,0,n-1)
        return nums
        

    def gsort(self,nums,left,right):
        if left>=right:
            return 
        
        mid=(left+right)//2
        self.gsort(nums,left,mid)
        self.gsort(nums,mid+1,right)
        res=[]
        i=left
        j=mid+1
        while i<=mid and j<=right:
            if nums[i]<=nums[j]:
                res.append(nums[i])
                i+=1
            else:
                res.append(nums[j])
                j+=1
        while i<=mid:
            res.append(nums[i])
            i+=1
        while j<=right:
            res.append(nums[j])
            j+=1
        for i in range(left,right+1):
            nums[i]=res[i-left]
        
if __name__=="__main__":
    test=Solution()
    print(test.mergeSort([2,3,2,8,2,4,2,51,0,2,5,2,1]))
  