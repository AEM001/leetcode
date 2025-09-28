def fast_sort(nums,left,right):
    if left>=right:
        return
    piv=nums[right]
    i=left
    for j in range(left,right):
        if nums[j]<piv:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
    nums[i],nums[right]=nums[right],nums[i]
    fast_sort(nums,left,i-1)
    fast_sort(nums,i+1,right)
    
def main():
	nums=[0,21,2,4,9,2,4,5,4,1,57,2,15,42,5,2,45,21,56,24,2,42,4]
	fast_sort(nums,0,len(nums)-1)
	print(nums)

if __name__ == "__main__":
	main()
