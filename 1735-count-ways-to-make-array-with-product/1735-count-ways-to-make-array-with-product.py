# class Solution:
#     def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        
#         @lru_cache(maxsize=None)
#         def dp(n ,k):
#             if k == 1 or n == 1 :
#                 return 1
            
#             ways = 0
#             for factor in range(1 , k+1) :
#                 if k % factor == 0 :
#                     ways += dp(n-1 , k//factor)
#                     ways %= (int(1e9)+7)
                
#             return ways%(10**9 + 7)


#         res = [0]*(len(queries))
#         for i , (n , k) in enumerate(queries) :
#             res[i] = dp(n,k)
        
#         return res

import math
from typing import List

class Solution:
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        res = []
        
        for n, k in queries:
            total_ways = 1
            temp_k = k
            
            # Find prime factorization of k
            d = 2
            while d * d <= temp_k:
                if temp_k % d == 0:
                    count = 0
                    while temp_k % d == 0:
                        count += 1
                        temp_k //= d
                    # Stars and Bars: math.comb(count + n - 1, count)
                    total_ways = (total_ways * math.comb(count + n - 1, count)) % MOD
                d += 1
                
            if temp_k > 1:
                # Prime factor with exponent 1
                total_ways = (total_ways * math.comb(1 + n - 1, 1)) % MOD
                
            res.append(total_ways)
            
        return res