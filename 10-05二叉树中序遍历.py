class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res=[]
        def mid(node):
            if not node:
                return 
            mid(node.left)
            # res.append(node.left.val)
            res.append(node.val)
            mid(node.right)
            # res.append(node.right.val)
        mid(root)
        return res
