class Solution:
    def selectionSort(self, nums: [int]) -> [int]:
        n=len(nums)
        for i in range(n-1):
            mini_i=i
            for j in range(i+1,n):
                if nums[j]<nums[mini_i]:
                    mini_i=j
            if mini_i!=i:
                nums[i],nums[mini_i]=nums[mini_i],nums[i]
        return nums


if __name__=="__main__":
    test=Solution()
    print(test.selectionSort([2,3,2,8,2,4,2,51,0,2,5,2,1]))

    