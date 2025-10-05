class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res=[]
        def tree(node):
            if not node:
               return
            res.append(node.val)
            tree(node.left)
            tree(node.right)
        tree(root)

        return res