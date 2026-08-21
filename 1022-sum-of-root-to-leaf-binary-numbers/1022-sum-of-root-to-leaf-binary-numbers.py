# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:

        if not root :
            return 0
        
        ans = []

        def dfs(node , string) :
            if not node :
                return

            if not node.left and not node.right :
                ans.append(string)
                return 

            if node.left :
                dfs(node.left , string + str(node.left.val))
            
            if node.right :
                dfs(node.right , string + str(node.right.val))
        
        dfs(root , str(root.val))

        total = 0
        for b_str in ans :
            total += int(b_str , 2)
    
        return total

            