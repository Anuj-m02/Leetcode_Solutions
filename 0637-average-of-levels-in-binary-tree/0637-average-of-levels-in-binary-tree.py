# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
        
        if not root :
            return []

        ans = []
        queue = deque([root])

        while queue :

            total = 0
            n = len(queue)
            for i in range(len(queue)) :
                node = queue.popleft()
                total += node.val

                if node.left :
                    queue.append(node.left)
                
                if node.right :
                    queue.append(node.right)
            

            ans.append(total/n)

        return ans 