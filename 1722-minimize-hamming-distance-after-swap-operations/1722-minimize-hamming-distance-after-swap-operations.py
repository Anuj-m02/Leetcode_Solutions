class DSU :
    def __init__(self , n) :
        self.parent = list(range(n))
        self.size = [1]*(n)
        self.comp = n
    
    def find(self , node) :
        if self.parent[node] != node :
            self.parent[node] = self.find(self.parent[node])
        
        return self.parent[node]
    
    def union(self , a , b) :
        root_a , root_b = self.find(a) , self.find(b)

        if root_a == root_b :
            return False
        
        self.size[root_a] += self.size[root_b]
        self.parent[root_b] = root_a
        self.comp -= 1

        return True


class Solution:
    def minimumHammingDistance(self, source: list[int], target: list[int], allowedSwaps: list[list[int]]) -> int:
        
        n = len(source)
        dsu = DSU(n)

        for u,v in allowedSwaps :
            dsu.union(u,v)
        
        # if dsu.comp == 1 :
        #     return 0
        
        grps = defaultdict(list)

        cnt = 0
        for i in range(n) :
            root = dsu.find(i)
            grps[root].append(i)
        
        ans = 0
        for indx in grps.values() :
            freq = defaultdict(int)

            for i in indx :
                freq[source[i]] += 1
            
            for i in indx :
                if freq[target[i]] > 0 :
                    freq[target[i]] -= 1
                
                else :
                    ans += 1
        

        return ans