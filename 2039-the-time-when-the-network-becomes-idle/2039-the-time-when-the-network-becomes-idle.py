class Solution:
    def networkBecomesIdle(self, edges: list[list[int]], patience: list[int]) -> int:
        
        n = len(patience)

        graph = defaultdict(list)

        for u,v in edges :
            graph[u].append(v)
            graph[v].append(u)
        
        dist = [-1]*n
        dist[0] = 0

        queue = deque([0])
        while queue :
            node = queue.popleft()
            for neighbour in graph[node] :
                if dist[neighbour] == -1 :
                    dist[neighbour] = dist[node] + 1
                    queue.append(neighbour)
        
        max_idle_time = 0

        for i in range(1 , n) :
            
            #round_trip time
            time = 2*dist[i]

            last_sent_time = ((time-1) // patience[i]) * (patience[i])
            last_mssg_return_time = last_sent_time + time

            max_idle_time = max(max_idle_time , last_mssg_return_time)
        
        return max_idle_time + 1
