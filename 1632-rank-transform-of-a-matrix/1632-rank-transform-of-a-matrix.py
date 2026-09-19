class Solution:
    def matrixRankTransform(self, matrix: list[list[int]]) -> list[list[int]]:
        
        n , m = len(matrix) , len(matrix[0])

        # 1. DSU to group equal values in the same row/column
        parent = {}
        def find(i):
            if parent.setdefault(i, i) != i:
                parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            root_i, root_j = find(i), find(j)
            if root_i != root_j:
                parent[root_i] = root_j

        # group equal values in same row
        for row in range(n):
            val_to_col = defaultdict(list)
            for col in range(m) :
                val_to_col[matrix[row][col]].append((row , col))
            for cells in val_to_col.values() :
                for i in range(1 , len(cells)):
                    union(cells[0] , cells[i])
        

        # Group equal values in same column
        for c in range(m):
            val_to_rows = defaultdict(list)
            for r in range(n):
                val_to_rows[matrix[r][c]].append((r, c))
            for cells in val_to_rows.values():
                for i in range(1, len(cells)):
                    union(cells[0], cells[i])
        
        graph = defaultdict(list)
        indegree = defaultdict(int)

        # rowwsie directed edges smaller ->larget
        for row in range(n) :
            sorted_row = sorted(set(matrix[row]))
            val_to_node = {}
            for col in range(m) :
                val_to_node[matrix[row][col]] = find((row , col))
            
            for i in range(len(sorted_row)-1) :
                u = val_to_node[sorted_row[i]]
                v = val_to_node[sorted_row[i+1]]
                graph[u].append(v)
                indegree[v] += 1
        
        # Column-wise directed edges (smaller -> larger)
        for c in range(m):
            sorted_col = sorted(set(matrix[r][c] for r in range(n)))
            val_to_node = {}
            for r in range(n):
                val_to_node[matrix[r][c]] = find((r, c))
            for i in range(len(sorted_col) - 1):
                u = val_to_node[sorted_col[i]]
                v = val_to_node[sorted_col[i + 1]]
                graph[u].append(v)
                indegree[v] += 1
        

        all_nodes = set(find((row , col)) for row in range(n) for col in range(m))

        queue = deque([node for node in all_nodes if indegree[node] == 0])
        rank_map = {}
        curr_rank = 1

        while queue :
            for _ in range(len(queue)) :
                curr = queue.popleft()
                rank_map[curr] = curr_rank

                for neighbour in graph[curr] :
                    indegree[neighbour] -= 1
                    if indegree[neighbour] == 0 :
                        queue.append(neighbour)
            
            curr_rank+=1
        
        res = [[0]*m for _ in range(n)]
        for row in range(n) :
            for col in range(m) :
                res[row][col] = rank_map[find((row , col))]
        
        return res
