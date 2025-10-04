class Solution:
    def selectionSort(self, nums: [int]) -> [int]:
        n=len(nums)
        for i in range(1,n):
            j=i
            while j>0 and nums[j]<nums[j-1]:
                nums[j],nums[j-1]=nums[j-1],nums[j]
                j-=1
 
        return nums

if __name__=="__main__":
    test=Solution()
    print(test.selectionSort([2,3,2,8,2,4,2,5,0,2,5,2,1]))

    