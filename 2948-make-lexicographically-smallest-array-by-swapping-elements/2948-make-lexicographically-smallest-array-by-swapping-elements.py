from collections import defaultdict , deque , Counter
import heapq
from functools import lru_cache

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
        
        # smallest array so whichever is smaller will be the parent
        if self.size[root_a] >= self.size[root_b] :
                

            self.size[root_a] += self.size[root_b]
            self.parent[root_b] = root_a

        else :
            root_a , root_b = root_b , root_a

            self.size[root_a] += self.size[root_b]
            self.parent[root_b] = root_a

        return True





class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        
        n = len(nums)

        sorted_indices_1 = []
        for indx , val in enumerate(nums) :
            sorted_indices_1.append((val , indx))
        
        sorted_indices_1.sort()
        sorted_indices = []
        for i in range(n) :
            sorted_indices.append(sorted_indices_1[i][1])


        # sorted_indices = sorted(range(n) , key = lambda i : nums[i])
        dsu = DSU(n)
        for i in range(n-1) :
            indx1 = sorted_indices[i]
            indx2 = sorted_indices[i+1]
            if nums[indx2] - nums[indx1] <= limit :
                dsu.union(indx1, indx2)
        
        # dsu = DSU(n)
        # for i in range(n):
        #     for j in range(i+1 , n) :

        #         if abs(nums[i] - nums[j]) <= limit :
        #             dsu.union(i,j)

        groups = defaultdict(list)
        # {parents : nodes}

        for i in range(n) :
            par = dsu.find(i)
            groups[par].append(i)
        
        print(groups)
        
        ans = [0]*(n)

        for par , indices in groups.items() :
            vals = sorted(nums[i] for i in indices)

            indices.sort()

            for indx , val in zip(indices , vals) :
                ans[indx] = val
        
        return ans

        

        # # find parent for each indx 
        # for i in range(n) :
        #     par = dsu.find(i)
        #     if par == i :
        #         ans.append(nums[i])
        #     else :
        #         ans.append(nums[par])
            
        # return ans

        