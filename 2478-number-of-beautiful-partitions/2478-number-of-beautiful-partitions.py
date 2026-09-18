from functools import lru_cache

class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        mod = int(1e9) + 7
        n = len(s)
        primes = set("2357")

        if s[0] not in primes or s[-1] in primes:
            return 0
        
        def is_valid_cut(indx):
            if indx == 0 or indx == n:
                return True
            return s[indx - 1] not in primes and s[indx] in primes

        @lru_cache(maxsize=None)
        def dp(indx, cnt):
            # Base case: reached end of string or formed all partitions
            if cnt == k:
                return 1 if indx <= n else 0
            if indx >= n:
                return 0

            # 1. Skip current index to scan for next valid cut point
            ans = dp(indx + 1, cnt) % mod
            
            # 2. If current index is a valid cut point, make a partition boundary here
            if is_valid_cut(indx):
                ans = (ans + dp(indx + minLength, cnt + 1)) % mod
            
            return ans % mod
        
        # Start at minLength with 1 partition completed (first partition starts at 0)
        return dp(minLength, 1)

# class Solution:
#     def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        
#         mod = int(1e9) + 7
#         n = len(s)
#         primes = set("2357")

#         if s[0] not in primes or s[-1] in primes :
#             return 0
        
#         def is_valid_cut(indx) :
#             if indx == 0 or indx == n :
#                 return True
            
#             return s[indx-1] not in primes and s[indx] in primes


#         @lru_cache(maxsize=None)
#         def dp(indx , cnt) :

#             if indx == n :
#                 if cnt == k :
#                     return 1
#                 else :
#                     return 0
            
#             if cnt == k or (n-indx) < (k-cnt)*minLength :
#                 return 0
            
#             ans = 0

#             # #skip this indx 
#             # ans += dp(indx+1 , cnt) % mod
            
#             # if current_indx is valid cut_point , try making partition here
#             if is_valid_cut(indx) :
#                 # nxt_cut = indx+minLength
#                 ans += dp(indx+minLength , cnt+1)%mod
            
#             return ans%mod
        
#         return dp(minLength , 1)


# # from functools import lru_cache

# # class Solution:
# #     def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
# #         mod = int(1e9) + 7
# #         n = len(s)
# #         primes = set("2357")

# #         # 1. Base check: 1st char MUST be prime, last char MUST be non-prime
# #         if s[0] not in primes or s[-1] in primes:
# #             return 0
        
# #         # Valid cut point: previous char is non-prime and current char is prime
# #         def is_valid_cut(i):
# #             if i == 0 or i == n:
# #                 return True
# #             return s[i - 1] not in primes and s[i] in primes

# #         @lru_cache(maxsize=None)
# #         def dp(indx, cnt):
# #             # Base Case: Reached the end with exactly k partitions
# #             if indx == n:
# #                 return 1 if cnt == k else 0
            
# #             # Early pruning
# #             if cnt == k or (n - indx) < (k - cnt) * minLength:
# #                 return 0

# #             ans = 0

# #             # Option A: Skip this index to find the next valid cut point
# #             ans = (ans + dp(indx + 1, cnt)) % mod

# #             # Option B: If current index is a valid cut point, make a partition here
# #             # and jump forward by `minLength`
# #             if is_valid_cut(indx):
# #                 ans = (ans + dp(indx + minLength, cnt + 1)) % mod

# #             return ans % mod
        
# #         return dp(0, 0)