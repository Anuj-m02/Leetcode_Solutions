class Solution:
    def countPairs(self, n: int, edges: list[list[int]], queries: list[int]) -> list[int]:
        
        degree = [0]*(n+1)
        shared_edges = defaultdict(int)

        for u,v in edges :
            degree[u] += 1
            degree[v] += 1
            state = (min(u,v) , max(u,v))
            shared_edges[state] += 1
        
        sorted_deg = sorted(degree[1:])
        ans = []

        for q in queries :

            left , right = 0 , n-1
            cnt = 0
            while left < right :
                if sorted_deg[left] + sorted_deg[right] > q :
                    cnt += (right-left)
                    right -= 1

                else :
                    left += 1
            
            for (u,v) , shared in shared_edges.items() :
                if degree[u] + degree[v] > q and degree[u]+degree[v] - shared <= q :
                    cnt -= 1
                
            ans.append(cnt)
        
        return ans
                