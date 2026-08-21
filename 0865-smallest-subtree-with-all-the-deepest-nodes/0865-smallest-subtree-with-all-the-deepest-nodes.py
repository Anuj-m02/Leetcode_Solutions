# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root :
            return None

        # curr_node , curr_lvl
        queue = deque([(root , 0)])
        parent_map = {root:None}

        lvl_to_nodes = defaultdict(list)
        deepest_lvl = 0
        # get the deepest lvl nodes
        while queue :
            curr_node , curr_lvl = queue.popleft()
            deepest_lvl = max(deepest_lvl , curr_lvl)

            lvl_to_nodes[curr_lvl].append(curr_node)

            if curr_node.left :
                queue.append((curr_node.left , curr_lvl+1))
                parent_map[curr_node.left] = curr_node
            if curr_node.right :
                queue.append((curr_node.right , curr_lvl + 1))
                parent_map[curr_node.right] = curr_node 

        # now that we have got the deepest lvl
        to_check = deepest_lvl-1
        req = set(lvl_to_nodes[deepest_lvl])
        queue = deque(lvl_to_nodes[to_check])
        ans = []

        while len(req) > 1 :
            parents = set()
            for node in req :
                parents.add(parent_map[node])
            req = parents
        
        return req.pop()


        # while queue :
        #     curr_node = queue.popleft()
        #     if curr_node.left in req :
        #         ans.append(curr_node)
        #         ans.append(curr_node.left)
        #     if curr_node.right in req :
        #         ans.append(curr_node)
        #         ans.append(curr_node.right)
        
        return ans



