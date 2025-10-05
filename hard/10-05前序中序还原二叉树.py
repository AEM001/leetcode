class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def tree(preorder,inorder,n):
            if n==0:
                return None
            k=0
            while inorder[k]!=preorder[0]:
                k+=1
            node=TreeNode(inorder[k])
            node.left=createTree(preorder[1:k+1],inorder[0:k],k)
            node.right=createTree(preorder[K+1:],inorder[k+1:],n-k-1)
            return node
        return tree(preorder,inorder,len(preorder))
