class Solution:
    def minimumTime(self, n: int, relations: list[list[int]], time: list[int]) -> int:

        graph = defaultdict(list)
        indegree = [0]*(n)

        for u , v in relations :
            u -= 1
            v -= 1
            graph[u].append(v)
            indegree[v] += 1

        max_time = [0]*(n)

        queue = deque([]) 
        for node in range(n) :
            if indegree[node] == 0 :
                max_time[node] = time[node]
                queue.append(node)
        
        while queue :
            curr_node = queue.popleft()

            for neighbour in graph[curr_node] :
                new_time = time[neighbour] + max_time[curr_node]
                max_time[neighbour] = max(max_time[neighbour] , new_time)
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0 :
                    queue.append(neighbour)
            
        return max(max_time)
