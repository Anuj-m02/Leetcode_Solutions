
from collections import defaultdict, Counter

class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, i: int) -> int:
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])  # Path compression
        return self.parent[i]

    def union(self, i: int, j: int) -> None:
        root_i = self.find(i)
        root_j = self.find(j)
        
        if root_i != root_j:
            # Union by size
            if self.size[root_i] < self.size[root_j]:
                root_i, root_j = root_j, root_i
            self.parent[root_j] = root_i
            self.size[root_i] += self.size[root_j]

class Solution:
    def largestComponentSize(self, nums: list[int]) -> int:
        
        n = len(nums)

        dsu = DSU(n)
        prime = defaultdict(int)

        def get_prime(n) :
            factors = []
            d = 2
            while d*d <= n :
                if n%d == 0 :
                    factors.append(d)
                    while n%d == 0 :
                        n //= d
                d += 1
            
            if n > 1 :
                factors.append(n)
            return factors


        for indx , num in enumerate(nums) :
            primes = get_prime(num)
            for p in primes :
                if p in prime :
                    dsu.union(prime[p] , indx)
                prime[p] = indx
        
        c = Counter()
        for indx in range(n) :
            c[dsu.find(indx)] += 1

        return max(c.values())
