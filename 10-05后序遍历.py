class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res=[]
        def last(node):
            if not node:
                return
            last(node.left)
            last(node.right)
            res.append(node.val)
        last(root)
        return res