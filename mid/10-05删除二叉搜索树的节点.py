# class Solution:
#     def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
#         def find(node,key):
#             if not node:
#                 return
#             if node.left or node.right and node.left.val==key or node.right.val==key:
#                 return node
#             if node.val<key:
#                 return find(node.right,key)
#             elif node.val>key:
#                 return find(node.left,key)
#         before=find(root,key)
       
#         if before.left and before.left.val==key:
#             node=before.left
#             before.left=delete(node)
#         elif before.right and before.right.val==key:
#             before.right=before.right

#         def delete(node):
#             if not (node.left and node.right):
#                 if node.left:
#                     return node.left
#                 else:
#                     return node.right
#             cur=node.right
#             while cur.left:
#                 cur=cur.left
#             if cur.val<node.left.val:
#                 cur.right=node.left
#             else:
#                 cur.left=node.left
#             return node.right
        
        
# 修正写法：
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        
        # 1. 特殊情况：树为空
        if not root:
            return None

        # 辅助函数：找到待删除节点的父节点和节点本身
        # 返回: (parent, target)
        def find_parent_and_target(node, key):
            parent = None
            current = node
            while current:
                if key == current.val:
                    return parent, current
                parent = current
                if key < current.val:
                    current = current.left
                else:
                    current = current.right
            return None, None # 未找到节点

        # 2. 查找父节点和目标节点
        parent, target = find_parent_and_target(root, key)
        
        # 3. 未找到目标节点
        if not target:
            return root
        
        # 4. 执行删除操作：根据目标节点的子节点情况分类讨论
        
        # 4a. 待删除节点没有左子节点或没有右子节点（含叶子节点）
        if not target.left or not target.right:
            # 要用来替代 target 的子节点
            # 如果 target.left 存在，就用它；否则用 target.right
            child = target.left if target.left else target.right

            if not parent:
                # 情况 A：待删除节点是根节点 (root)
                return child # 新的根节点就是 child
            
            # 情况 B：待删除节点是普通节点
            if target == parent.left:
                parent.left = child
            else:
                parent.right = child
            
            return root

        # 4b. 待删除节点同时拥有左右子节点
        # 策略：找到右子树中的最小节点（后继节点）来替换 target
        
        # i. 找到后继节点及其父节点
        successor_parent = target
        successor = target.right
        while successor.left:
            successor_parent = successor
            successor = successor.left
        
        # ii. 替代目标节点：将后继节点从其原位置移除，并放到 target 的位置上
        
        # A. 后继节点（successor）是 target 的右子节点
        if successor == target.right:
            # 1. 后继节点的左子节点连接到 target 的左子节点
            successor.left = target.left
            # 2. 如果 target 是根节点，返回 successor 作为新根
            if not parent:
                return successor
            # 3. 将 parent 指针指向 successor
            if target == parent.left:
                parent.left = successor
            else:
                parent.right = successor
            
            return root
        
        # B. 后继节点（successor）不是 target 的右子节点（即它是 target.right 的左子树最深处）
        else:
            # 1. 将后继节点的右子节点连接到后继节点父节点（successor_parent）的左指针
            #    注意：successor 是后继节点父节点的左子节点，且 successor 最多只有一个右子节点
            successor_parent.left = successor.right
            
            # 2. 将 target 的左右子树连接到 successor 上
            successor.left = target.left
            successor.right = target.right

            # 3. 将 parent 指针指向 successor
            if not parent:
                return successor # target 是根节点
            
            if target == parent.left:
                parent.left = successor
            else:
                parent.right = successor
            
            return root
        
# 递归写法
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        
        # 递归删除函数，返回删除节点后的新子树根节点
        def dele(node: TreeNode, key: int) -> TreeNode:
            if not node:
                # 1. 节点不存在，返回None
                return None
            
            # 2. 查找待删除节点
            if key < node.val:
                # 键小于当前节点值，递归左子树
                node.left = dele(node.left, key)
                return node
            elif key > node.val:
                # 键大于当前节点值，递归右子树
                node.right = dele(node.right, key)
                return node
            
            # 3. 找到待删除节点 (key == node.val)
            else:
                # 3a. 待删除节点没有左子节点或没有右子节点（包含叶子节点情况）
                if not node.left:
                    # 返回右子节点，接替当前节点的位置
                    # 如果右子节点为None（叶子节点），则相当于删除
                    return node.right
                if not node.right:
                    # 返回左子节点，接替当前节点的位置
                    return node.left
                
                # 3b. 待删除节点同时拥有左右子节点
                # 策略：用右子树的最小节点（后继节点）来替换当前节点
                
                # 1. 找到右子树中的最小节点 (即最左侧的节点)
                successor = node.right
                while successor.left:
                    successor = successor.left
                
                # 2. 将后继节点的值赋给当前节点（逻辑上实现替换）
                node.val = successor.val
                
                # 3. 在右子树中递归删除后继节点（因为其值已经移动到当前位置）
                # 这一步很重要，因为后继节点最多只有一个右子节点，删除它很简单
                node.right = dele(node.right, successor.val) 
                
                return node
                
        # 从根节点开始调用递归删除函数
        return dele(root, key)

            