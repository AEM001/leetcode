class Solution:
    def quickSort(self, nums: [int]) -> [int]:
        n=len(nums)
        self.sort(nums,0,n-1)
        return nums
        
    def sort(self,nums,left,right):
        if left>=right:
            return 
        piv=nums[right]
        i=left
        for j in range(left,right):
            if nums[j]<piv:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
        nums[i],nums[right]=nums[right],nums[i]
        self.sort(nums,left,i-1)
        self.sort(nums,i+1,right)
        
if __name__=="__main__":
    test=Solution()
    print(test.quickSort([2,3,2,8,2,4,2,51,0,2,5,2,1]))