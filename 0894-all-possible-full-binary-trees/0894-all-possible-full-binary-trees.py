# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        
#         if n%2 == 0 :
#             return []

#         @lru_cache(maxsize=None)
#         def dp(node) :

#             if node == 1 :
#                 return [TreeNode(0)]
            
#             res = []
#             for i in range(1 , node , 2) :
#                 left_tree = dp(i)
#                 right_tree = dp(node-1-i)

#                 for left in left_tree :
#                     for right in right_tree :
#                         root = TreeNode(0 , left , right)
#                         res.append(root)
            
#             return res
        
#         return dp(n)

from functools import lru_cache
from typing import List, Optional

class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        # A full binary tree must have an odd number of nodes
        if n % 2 == 0:
            return []

        @lru_cache(maxsize=None)
        def dp(node: int) -> List[Optional[TreeNode]]:
            if node == 1:
                return [TreeNode(0)]
            
            res = []
            # Left subtree size `i` must be odd, ranging from 1 to node - 2
            for i in range(1, node, 2):
                left_trees = dp(i)
                right_trees = dp(node - 1 - i)
                
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(0, left, right)
                        res.append(root)
            return res

        return dp(n)