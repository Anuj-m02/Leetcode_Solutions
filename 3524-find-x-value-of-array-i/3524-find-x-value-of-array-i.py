class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        

        # x goes from 0 to upto k-1
        n = len(nums)
        ans = [0]*(k)

        @lru_cache(maxsize=None)
        def dp(indx , rem) :

            if indx == n :
                return {}
            
            val = nums[indx]%k
            count = {val : 1}

            nxt_count = dp(indx+1 , rem)
            for prev_rem , cnt in nxt_count.items() :
                new_rem = (val*prev_rem)%k
                count[new_rem] = count.get(new_rem , 0) + cnt
            
            return count
        

        for indx in range(n) :
            count = dp(indx , k)
            for rem,cnt in count.items() :
                ans[rem] += cnt
        
        return ans

# from functools import lru_cache

# class Solution:
#     def resultArray(self, nums: list[int], k: int) -> list[int]:
#         n = len(nums)
#         ans = [0] * k

#         @lru_cache(maxsize=None)
#         def dp(i: int, rem: int) -> int:
#             """
#             Returns the number of subarrays ENDING at index i 
#             whose product modulo k equals rem.
#             """
#             val = nums[i] % k
            
#             # Base choice: single-element subarray [nums[i]]
#             count = 1 if val == rem else 0
            
#             if i == 0:
#                 return count

#             # Extend subarrays from index i - 1
#             # We look for previous remainder 'prev_rem' such that (prev_rem * val) % k == rem
#             for prev_rem in range(k):
#                 if (prev_rem * val) % k == rem:
#                     count += dp(i - 1, prev_rem)
                    
#             return count

#         # Accumulate results across all ending indices i and all remainders rem
#         for i in range(n):
#             for rem in range(k):
#                 ans[rem] += dp(i, rem)

#         return ans