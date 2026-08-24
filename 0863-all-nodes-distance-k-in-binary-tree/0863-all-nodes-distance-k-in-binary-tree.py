# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def parents(self,root,parents_track,target) :
        queue = deque([(root)])
        while queue :
            node = queue.popleft()
            if node.left :
                queue.append(node.left)
                parents_track[node.left] = node
            if node.right :
                queue.append(node.right)
                parents_track[node.right] = node

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parents_track = {}
        self.parents(root,parents_track,target)
        visited = set()
        queue = deque([(target , 0)])
        ans = []
        visited.add(target)
        dis = 0
        while queue :
            size = len(queue)
            if queue[0][1] == k:
                return [node.val for node, lvl in queue]
            for i in range(size):
                node , lvl = queue.popleft()
                # if lvl == k :
                #     ans.append(node)
                if node.left and node.left not in visited :
                    queue.append((node.left , lvl+1))
                    visited.add(node.left)
                if node.right and node.right not in visited :
                    queue.append((node.right , lvl+1))
                    visited.add(node.right)
                if node in parents_track and parents_track[node] not in visited :
                    queue.append((parents_track[node] , lvl+1))
                    visited.add(parents_track[node])
            dis += 1
        return ans

