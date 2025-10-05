class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # def make(nums,left,right,root):
        #     if not root:
        #         mid=(left+right)//2
        #         root=TreeNode(nums[mid])
        #     if left==mid:
        #         return TreeNode(nums[left])
        #     if mid==right:
        #         return TreeNode(nums[right])
        #     root.left=make(nums,left,mid,root)
        #     root.right=make(nums,mid+1,right,root)
        #     return root
        # return make(nums,0,len(nums)-1,None)


        def make(nums,left,right):
            if left>right:
                return
            mid=left+(right-left)//2
            root=TreeNode(nums[mid])
            root.left=make(nums,left,mid-1)
            root.right=make(nums,mid+1,right)
            return root
        return make(nums,0,len(nums)-1)
