from collections import defaultdict , deque , Counter
import heapq
from functools import lru_cache

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        if not root :
            return 0

        @lru_cache(None)
        def dp(node , dir , length) :

            if not node :
                return 0
            
            ans = length
            # at each node we have option
            # follow the direction 
            # or start from next node 
            # ans = max(ans , length)

            if dir == 0 :
                ans =  max( ans , 
                # go to right
                dp(node.right , 1 , length + 1) ,
                dp(node.left , 0 , 1))
            
            else :
                ans =  max( ans ,
                    dp(node.left , 0 , length+1) , dp(node.right , 1 , 1)
                )
            # if dir == -1 :
            #     # start from here
            #     ans = max(1 + dp(node.left , 1) , 1 + dp(node.right , 0))
            
            # elif dir == 0 :
            #     ans = 1 + dp(node.right , 0)
            # else :
            #     ans = 1 + dp(node.left , 1)


            # # also start from its child node

            # ans = max(ans , dp(node.left , -1) , dp(node.right , -1))

            return ans
        
        return max(dp(root.left , 0 , 1) , dp(root.right , 1 , 1))


# from collections import defaultdict, deque, Counter
# import heapq
# from typing import Optional

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def longestZigZag(self, root: Optional[TreeNode]) -> int:

#         def dfs(node, dir, length):
#             if not node:
#                 return 0
            
#             # Record length reached at current node
#             ans = length

#             # If dir == 0: came by going left -> next must go right to extend (dir = 1)
#             # OR restart going left from left child with length = 1 (dir = 0)
#             if dir == 0:
#                 ans = max(ans, 
#                           dfs(node.right, 1, length + 1), 
#                           dfs(node.left, 0, 1))
#             else:
#                 ans = max(ans, 
#                           dfs(node.left, 0, length + 1), 
#                           dfs(node.right, 1, 1))

#             return ans
        
#         if not root:
#             return 0

#         # Start from root going left (dir=0) and going right (dir=1) with length 0
#         return max(dfs(root.left, 0, 1), dfs(root.right, 1, 1))