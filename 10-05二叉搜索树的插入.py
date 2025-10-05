class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
#         def ins(node,val):
#             if not node:
#                 return TreeNode(val)
#             if node.val==val:
#                 return node
#             elif node.val<val:
#                 return ins(node.right,val)
#             else:
#                 return ins(node.left,val)
#         return ins(root,val)


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            # 当前子树为空，直接创建新节点并返回
            return TreeNode(val)

        if val < root.val:
            # 待插入值小于当前节点值，递归插入到左子树
            root.left = self.insertIntoBST(root.left, val)
        elif val > root.val:
            # 待插入值大于当前节点值，递归插入到右子树
            root.right = self.insertIntoBST(root.right, val)
        # 如果 val == root.val，不插入（不允许重复），直接返回原树
        return root