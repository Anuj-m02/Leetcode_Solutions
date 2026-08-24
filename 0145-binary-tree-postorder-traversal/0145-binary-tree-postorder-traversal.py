# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:


        def help(node , ans) :
            if not node :
                return None
            
            help(node.left , ans)
            help(node.right , ans)
            ans.append(node.val)
        ans = []
        help(root , ans)
        return ans
        # stack1 = []
        # stack2 = []
        # ans = []
        # if root == None :
        #     return ans
        # stack1.append(root)
        # while stack1 :
        #     node = stack1.pop()
        #     stack2.append(node)
        #     if node.left != None :
        #         stack1.append(node.left)
        #     if node.right != None :
        #         stack1.append(node.right)
        # while stack2 :
        #     node = stack2.pop()
        #     ans.append(node.val)
        # return ans