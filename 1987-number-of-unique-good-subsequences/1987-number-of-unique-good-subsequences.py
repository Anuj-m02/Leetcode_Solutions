# from collections import defaultdict , deque , Counter
# import heapq
# from functools import lru_cache


# class Solution:
#     def numberOfUniqueGoodSubsequences(self, binary: str) -> int:

#         n = len(binary)
#         mod = 10**9 + 7

#         unique = set()

#         def dp(indx , prev , started) :
            
#             if indx == n :
#                 return 0
            
#             # skip this indx
#             ans = dp(indx+1 , prev , started)

#             if binary[indx] == "0" :
#                 if not started :
#                     uniqu

class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        mod = 10**9 + 7

        n = len(binary)

        nxt_one = [-1]*(n)
        nxt_zero = [-1]*(n)

        pos_zero , pos_one = -1 , -1

        for i in range(n-1 , -1 , -1) :
            if binary[i] == "0" :
                pos_zero = i
            else :
                pos_one = i
            nxt_zero[i] = pos_zero
            nxt_one[i] = pos_one
        
        @lru_cache(maxsize=None)
        def dp(indx  , started) :

            if indx >= n :
                return 0
            
            ans = 0

            if not started :
                # pick only one
                indx1 = nxt_one[indx]
                if indx1 != -1 :
                    ans += (1 + dp(indx1+1 , True))%mod
                
            else:

                # can pick zero
                indx1 = nxt_zero[indx]
                if indx1 != -1 :

                    ans += (1 + dp(indx1+1 , True))%mod
                
                # can pick one alos
                indx2 = nxt_one[indx]
                if indx2 != -1 :
                    ans += (1 + dp(indx2 + 1 , True))%mod
            
            return ans
        
        if "0" in binary :
            return dp(0 , False) + 1
        
        else :
            return dp(0 , False)

