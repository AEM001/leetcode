def fast_sort(nums,head,tail):
	# 当区间长度为0或1时直接返回
	if head >= tail:
		return
	# 使用“挖坑法/移动枢轴”的分区方式，严格沿用你“枢轴与左右指针元素交换并移动枢轴”的思路
	i = head
	j = tail
	piv = head
	while i < j:
		# 从右边找第一个小于枢轴的元素
		while i < j and nums[j] >= nums[piv]:
			j -= 1
		if i < j:
			# 把这个更小的元素放到枢轴位置，枢轴移动到 j
			nums[piv], nums[j] = nums[j], nums[piv]
			piv = j
		# 从左边找第一个大于枢轴的元素
		while i < j and nums[i] <= nums[piv]:
			i += 1
		if i < j:
			# 把这个更大的元素放到枢轴位置，枢轴移动到 i
			nums[piv], nums[i] = nums[i], nums[piv]
			piv = i

	# 以最终枢轴位置切分左右区间
	fast_sort(nums, head, piv - 1)
	fast_sort(nums, piv + 1, tail)

def main():
	nums=[0,21,2,4,9,2,4,5,4,1,57,2,15,42,5,2,45,21,56,24,2,42,4]
	fast_sort(nums,0,len(nums)-1)
	print(nums)

if __name__ == "__main__":
	main()
