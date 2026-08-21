# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        

        # first traveersal for parent mapping
        parent_map = {root : None}
        # curr_node , curr_lvl
        queue = deque([(root , 0)])
        parent_map = {root:None}
        val_to_node = {root.val : root}

        lvl_to_nodes = defaultdict(list)
        deepest_lvl = 0
        # get the deepest lvl nodes
        while queue :
            curr_node , curr_lvl = queue.popleft()
            deepest_lvl = max(deepest_lvl , curr_lvl)
            val_to_node[curr_node.val] = curr_node

            lvl_to_nodes[curr_lvl].append(curr_node)

            if curr_node.left :
                queue.append((curr_node.left , curr_lvl+1))
                parent_map[curr_node.left] = curr_node
            if curr_node.right :
                queue.append((curr_node.right , curr_lvl + 1))
                parent_map[curr_node.right] = curr_node 
        
        startnode = val_to_node[startValue]
        queue = deque([(startnode , "")])
        vis = set()
        vis.add(startnode)

        while queue :
            node , curr_path = queue.popleft()
            if node == val_to_node[destValue] :
                return curr_path
            
            if node.left and node.left not in vis :
                vis.add(node.left)
                queue.append((node.left , curr_path + "L"))
            
            if node.right and node.right not in vis :
                vis.add(node.right)
                queue.append((node.right , curr_path + "R"))
            
            if parent_map[node] and parent_map[node] not in vis :
                vis.add(parent_map[node])
                queue.append((parent_map[node] , curr_path + "U"))
        
# class Solution:
#     def getDirections(self, root: Optional[TreeNode],
#                       startValue: int,
#                       destValue: int) -> str:

#         def find_path(node, target, path):
#             if not node:
#                 return False

#             if node.val == target:
#                 return True

#             path.append("L")
#             if find_path(node.left, target, path):
#                 return True
#             path.pop()

#             path.append("R")
#             if find_path(node.right, target, path):
#                 return True
#             path.pop()

#             return False

#         path_start = []
#         path_dest = []

#         find_path(root, startValue, path_start)
#         find_path(root, destValue, path_dest)

#         i = 0

#         # Find common path from root
#         while (i < len(path_start) and
#                i < len(path_dest) and
#                path_start[i] == path_dest[i]):
#             i += 1

#         # From start node, go UP to the LCA
#         result = "U" * (len(path_start) - i)

#         # From LCA, follow path to destination
#         result += "".join(path_dest[i:])

#         return result