class Solution:
    def shellSort(self, nums: [int]) -> [int]:
        n=len(nums)
        gap=n//2
        while gap>0:
            for i in range(gap,n):
                j=i
                while j>=gap and nums[j-gap]>nums[j]:
                    nums[j-gap],nums[j]=nums[j],nums[j-gap]
                    j-=gap
            gap=gap//2
        return nums

if __name__=="__main__":
    test=Solution()
    print(test.shellSort([2,3,2,8,2,4,2,9,41,14,1,0,2,5,2,1]))
