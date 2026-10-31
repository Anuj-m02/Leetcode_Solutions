class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        
        parent = list(range(n))
        size = [1]*(n)

        def find(node) :
            if parent[node] != node :
                parent[node] = find(parent[node])
            return parent[node]
        
        def union(a , b) :
            root_a , root_b = find(a) , find(b)
            if root_a == root_b :
                return False
            
            parent[root_a] = root_b
            size[root_b] += size[root_a]
        

        for u,v in edges :
            union(u,v)
        
        root_a , root_b = find(source) , find(destination)

        return root_a == root_b