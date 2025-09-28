def fast_sort(nums,left,right):
    if left>=right:
        return
    piv=left
    i,j=left,right
    while(i<j):
        while i<j and nums[j]>nums[piv]:
            j-=1
        if i<j:
            nums[j],nums[piv]=nums[piv],nums[j]
            piv=j
        while i<j and nums[i]<nums[piv]:
            i+=1
        if i<j:
            nums[i],nums[piv]=nums[piv],nums[i]
            piv=i
    fast_sort(nums,left,piv-1)
    fast_sort(nums,piv+1,right)

    

def main():
	nums=[0,21,2,4,9,2,4,5,4,1,57,2,15,42,5,2,45,21,56,24,2,42,4]
	fast_sort(nums,0,len(nums)-1)
	print(nums)

if __name__ == "__main__":
	main()
