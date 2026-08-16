# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def minCameraCover(self, root: Optional[TreeNode]) -> int:
        
#         def dp(node , covered) :
#             if not node :
#                 # if has_cam :
#                 #     return float("inf")
#                 return 0
            
#             # place camera
#             place = 1 + dp(node.left , True) + dp(node.right , True)

#             # dont place camera 
#             if covered :
#                 # if node alrdy covered up , then childrence are not covred
#                 not_place = dp(node.left , False) + dp(node.right , False)
#                 return min(place , not_place)
            
#             else :
#                 # node is not covered so if we are not placeing cam here then at least one child must have camera

# # Sub-option A: Put camera on left child
#                 left_cam = (1 + dp(node.left.left, True) + dp(node.left.right, True)) + dp(node.right, False) if node.left else float("inf")

#                 # Sub-option B: Put camera on right child
#                 right_cam = dp(node.left, False) + (1 + dp(node.right.left, True) + dp(node.right.right, True)) if node.right else float("inf")

#                 return min(place, left_cam, right_cam)
        
#         if not root :
#             return 0

#         return dp(root , False)


from functools import lru_cache

class Solution:
    def minCameraCover(self, root):

        INF = 10**9

        @lru_cache(None)
        def dp(node, covered):

            if not node:
                return 0

            # Put camera at current node
            take = (
                1
                + dp(node.left, 1)
                + dp(node.right, 1)
            )

            if covered:
                # Current node is already covered.
                # We can either take camera or leave it.
                not_take = (
                    dp(node.left, 0)
                    + dp(node.right, 0)
                )

                return min(take, not_take)

            else:
                # Current node is NOT covered.
                # If we don't put camera here, at least one child
                # must have a camera.
                
                not_take = INF

                # Camera on left child
                if node.left:
                    left_camera = (
                        1
                        + dp(node.left.left, 1)
                        + dp(node.left.right, 1)
                        + dp(node.right, 0)
                    )
                    not_take = min(not_take, left_camera)

                # Camera on right child
                if node.right:
                    right_camera = (
                        1
                        + dp(node.right.left, 1)
                        + dp(node.right.right, 1)
                        + dp(node.left, 0)
                    )
                    not_take = min(not_take, right_camera)

                return min(take, not_take)

        # Root has no parent, so it is initially not covered.
        return dp(root, 0)