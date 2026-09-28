class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j

class Solution:
    def maxAlternatingSum(self, nums: List[int], swaps: List[List[int]]) -> int:
        
        n = len(nums)
        dsu = DSU(n)

        for indx , (i,j) in enumerate(swaps) :
            dsu.union(i,j)
        
        comp_even_cnt = defaultdict(int)
        # for each indx get parent : {indx to all which it can be swapped with}
        d = defaultdict(list)
        for i in range(n) :
            root = dsu.find(i)
            d[root].append(nums[i])
            if i%2 == 0 :
                comp_even_cnt[root] += 1




        total = 0
        for root in d :
            val = d[root]
            val.sort(reverse=True)

            even_cnt = comp_even_cnt[root]

            sum_even_pos = sum(val[:even_cnt])
            sum_odd_pos = sum(val[even_cnt :])

            total += sum_even_pos - sum_odd_pos
        
        return total
