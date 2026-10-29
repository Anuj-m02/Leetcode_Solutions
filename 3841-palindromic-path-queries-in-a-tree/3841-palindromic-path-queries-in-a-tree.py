# # class Solution:
# #     def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        
# #         graph = defaultdict(list)
# #         for u,v in edges :
# #             graph[u].append(v)
# #             graph[v].append(u)
        

# #         s_list = list(s)
# #         ans = []

# #         for query in queries :
# #             parts = query.split()
# #             if parts[0] == "update" :
# #                 u = int(parts[1])
# #                 c = parts[2]
# #                 s_list[u] = c
            
# #             else :
# #                 u = int(parts[1])
# #                 v = int(parts[2])

# #                 parent = {}
# #                 visited = {u}
# #                 queue = deque([u])

# #                 while queue :
# #                     curr = queue.popleft()
# #                     if curr == v :
# #                         break
                    
# #                     for neighbour in graph[curr] :
# #                         if neighbour not in visited :
# #                             visited.add(neighbour)
# #                             parent[neighbour] = curr
# #                             queue.append(neighbour)
                
# #                 path_chars = []
# #                 curr = v
# #                 while curr != u :
# #                     path_chars.append(s_list[curr])
# #                     curr = parent[curr]
                
# #                 path_chars.append(s_list[u])

# #                 if path_chars == path_chars[::-1] :
# #                     ans.append("true")
# #                 else :
# #                     ans.append("false")

# #         return ans

# from collections import deque

# class Solution:
#     def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
#         # Build adjacency list
#         adj = [[] for _ in range(n)]
#         for u, v in edges:
#             adj[u].append(v)
#             adj[v].append(u)
            
#         s_list = list(s)
#         ans = []
        
#         for query in queries:
#             parts = query.split()
#             if parts[0] == "update":
#                 u = int(parts[1])
#                 c = parts[2]
#                 s_list[u] = c
#             else:  # query u v
#                 u = int(parts[1])
#                 v = int(parts[2])
                
#                 # BFS to find path from u to v
#                 parent = {}
#                 visited = {u}
#                 queue = deque([u])
                
#                 while queue:
#                     curr = queue.popleft()
#                     if curr == v:
#                         break
#                     for neighbor in adj[curr]:
#                         if neighbor not in visited:
#                             visited.add(neighbor)
#                             parent[neighbor] = curr
#                             queue.append(neighbor)
                            
#                 # Reconstruct path and collect characters
#                 path_chars = []
#                 curr = v

#                 freq = [0]*(26)

#                 while curr != u:
#                     path_chars.append(s_list[curr])
#                     freq[ord(s_list[curr]) - ord("a")] += 1
#                     curr = parent[curr]
#                 path_chars.append(s_list[u])
#                 freq[ord(s_list[u]) - ord("a")] += 1
                
#                 # # Check palindrome condition using a 26-bit bitmask
#                 # mask = 0
#                 # for ch in path_chars:
#                 #     mask ^= (1 << (ord(ch) - ord('a')))
                    
#                 # # Valid palindrome if mask has at most one set bit
#                 # ans.append((mask & (mask - 1)) == 0)

#                 # for palidnorme iff atmost 1 odd cnt
#                 odd_cnt = sum(1 for cnt in freq if cnt%2)
#                 ans.append(odd_cnt <= 1)




#         return ans

class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        # Binary Lifting setup
        LOGN = 17
        up = [[0] * LOGN for _ in range(n)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0
        
        s_chars = list(s)
        node_mask = [1 << (ord(ch) - ord('a')) for ch in s_chars]
        path_from_root = [0] * n
        
        # DFS for LCA binary lifting and Euler Tour order
        stack = [(0, -1, 0)]  # (u, p, state)
        # Using iterative DFS to handle large inputs smoothly in Python
        order = []
        
        # Pre-DFS to compute depth, binary lifting, tin/tout
        parent = [-1] * n
        depth = [0] * n
        euler_order = []
        
        # Simple iterative DFS
        st = [(0, -1)]
        visited = [False] * n
        adj_iter = [iter(adj[i]) for i in range(n)]
        
        tin = [0] * n
        tout = [0] * n
        timer = 1
        
        path_from_root[0] = node_mask[0]
        st = [0]
        tin[0] = timer
        timer += 1
        
        while st:
            u = st[-1]
            try:
                v = next(adj_iter[u])
                if v != up[u][0]:
                    up[v][0] = u
                    depth[v] = depth[u] + 1
                    path_from_root[v] = path_from_root[u] ^ node_mask[v]
                    tin[v] = timer
                    timer += 1
                    st.append(v)
            except StopIteration:
                tout[u] = timer - 1
                st.pop()
                
        # Fill binary lifting table
        for j in range(1, LOGN):
            for i in range(n):
                up[i][j] = up[up[i][j-1]][j-1]
                
        def get_lca(u: int, v: int) -> int:
            if depth[u] < depth[v]:
                u, v = v, u
            for j in range(LOGN - 1, -1, -1):
                if depth[u] - (1 << j) >= depth[v]:
                    u = up[u][j]
            if u == v:
                return u
            for j in range(LOGN - 1, -1, -1):
                if up[u][j] != up[v][j]:
                    u = up[u][j]
                    v = up[v][j]
            return up[u][0]

        # Binary Indexed Tree (Fenwick Tree) for Point Queries & Range XOR Updates
        bit = [0] * (n + 2)
        
        def bit_update(idx: int, val: int):
            while idx <= n + 1:
                bit[idx] ^= val
                idx += idx & (-idx)
                
        def bit_query(idx: int) -> int:
            res = 0
            while idx > 0:
                res ^= bit[idx]
                idx -= idx & (-idx)
            return res
            
        def range_xor_update(l: int, r: int, val: int):
            bit_update(l, val)
            bit_update(r + 1, val)

        def get_current_root_mask(u: int) -> int:
            return path_from_root[u] ^ bit_query(tin[u])

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                new_ch = parts[2]
                old_mask = node_mask[u]
                new_mask = 1 << (ord(new_ch) - ord('a'))
                diff = old_mask ^ new_mask
                
                if diff != 0:
                    node_mask[u] = new_mask
                    # Subtree update in Euler Tour interval [tin[u], tout[u]]
                    range_xor_update(tin[u], tout[u], diff)
            else:
                u = int(parts[1])
                v = int(parts[2])
                lca = get_lca(u, v)
                
                mask_u = get_current_root_mask(u)
                mask_v = get_current_root_mask(v)
                
                # Path XOR = mask_u ^ mask_v ^ node_mask[lca]
                path_mask = mask_u ^ mask_v ^ node_mask[lca]
                
                # At most one set bit check
                ans.append((path_mask & (path_mask - 1)) == 0)
                
        return ans