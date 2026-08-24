class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        n = len(isConnected)
        graph = defaultdict(list)

        for i in range(n) :
            for j in range(n) :
                if i != j :
                    if isConnected[i][j] == 1 :
                        graph[i].append(j)
                        graph[j].append(i)
        
        queue = deque([])
        vis = [0]*(n)
        cnt = 0
        for node in range(n):
            if not vis[node] :
                cnt += 1
                queue = deque([node])
                while queue :
                    curr_node = queue.popleft()
                    for neighbour in graph[curr_node] :
                        if not vis[neighbour] :
                            vis[neighbour] = 1
                            queue.append(neighbour)
        
        return cnt