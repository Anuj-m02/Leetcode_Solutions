class Solution:
    # eccentricity of i = max(d(i,x),d(i,y)), diameter (x,y) 
    def timeTaken(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)+1
        adj = [[] for i in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        def xfs(s): # return distance
            d = [-1]*n
            q = [s]
            d[s] = 2-s%2 # count the weight of source
            while q:
                v = q.pop()
                for u in adj[v]:
                    if d[u]!=-1: continue
                    d[u] = d[v]+2-(u&1)
                    q.append(u)
            return d
        # find diameter
        d0 = xfs(0)
        x = d0.index(max(d0))
        dx = xfs(x)
        y = dx.index(max(dx))
        dy = xfs(y)
        ans = [max(dx[i],dy[i])-(2-i%2) for i in range(n)]
        return ans


        