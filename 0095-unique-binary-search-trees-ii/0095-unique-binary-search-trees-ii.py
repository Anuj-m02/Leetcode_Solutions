# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
#         if n == 0 :
#             return []
#         memo = {}
#         def help(start,end):
#             if (start,end) in memo :
#                 return memo[(start,end)]
#             trees = []
#             if start>end :
#                 trees.append(None)
#                 return trees
#             for root_val in range(start,end+1):
#                 left_trees = help(start,root_val-1)
#                 right_trees = help(start,root_val+1)
#                 for left in left_trees:
#                     for right in right_trees:
#                         root = TreeNode(root_val,left,right)
#                         trees.append(root)
#             memo[(start,end)] = trees
#             return trees
#         return help(1,n)

from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
            
        memo = {}

        def help(start, end):
            if start > end:
                return [None]
                
            if (start, end) in memo:
                return memo[(start, end)]

            trees = []
            for root_val in range(start, end + 1):
                # Left subtrees must range from start to root_val - 1
                left_trees = help(start, root_val - 1)
                
                # Right subtrees must range from root_val + 1 to end (FIXED)
                right_trees = help(root_val + 1, end)

                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(root_val, left, right)
                        trees.append(root)

            memo[(start, end)] = trees
            return trees

        return help(1, n)