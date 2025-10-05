class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def find(node,val):
            if not node:
                return None
            if node.val==val:
                return node
            elif node.val<val:
                return find(node.right,val)
            else:
                return find(node.left,val)
        return find(root,val)
            