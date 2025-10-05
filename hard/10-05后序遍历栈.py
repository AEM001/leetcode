class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        二叉树后序遍历（非递归/显式栈实现）
        参数:
            root: Optional[TreeNode]，二叉树的根节点
        返回:
            List[int]，后序遍历的节点值列表
        """
        res = []        # 用于存储遍历结果
        stack = []      # 显式栈，用于模拟递归过程
        prev = None     # 记录上一个访问的节点，用于判断右子树是否已访问

        while root or stack:  # 只要当前节点不为空或栈不为空就继续遍历
            # 一直向左走，将所有左子节点入栈
            while root:
                stack.append(root)      # 当前节点入栈
                root = root.left        # 继续遍历左子树

            node = stack.pop()          # 弹出栈顶节点，准备访问或遍历其右子树

            # 判断是否可以访问当前节点
            # 1. 没有右子树
            # 2. 右子树已经访问过（即上一次访问的节点是当前节点的右子节点）
            if not node.right or node.right == prev:
                res.append(node.val)    # 访问当前节点
                prev = node             # 更新上一次访问的节点
                root = None             # 当前节点已访问，重置root，防止重复入栈
            else:
                # 右子树还未访问，当前节点重新入栈，转而遍历右子树
                stack.append(node)
                root = node.right

        return res