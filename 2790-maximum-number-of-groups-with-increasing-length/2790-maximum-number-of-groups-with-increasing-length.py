# # class Solution:
# #     def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
        
# #         n = len(usageLimits)
# #         arr = []
# #         for indx , val in enumerate(usageLimits) :
# #             arr.append((val , indx))
        
# #         arr.sort()

# #         def check(mid , arr) :
            
# #             cnt = 0
# #             available = 0
# #             # we need at least 1 + 2 + 3 + 4 ... + mid elemnts so total n*(n+1)//2
# #             for limit in sorted(usageLimits) :
# #                 available += min(limit , mid)
            
# #             return available >= (mid+2)*(mid+1)//2



# #         low , high = 0 , n
# #         ans = 0
# #         while low <= high :
# #             mid = (low+high)//2
# #             if check(mid , arr) :
# #                 low = mid+1
# #                 ans = mid
# #             else :
# #                 high = mid-1
        
# #         return ans

# class Solution:
#     def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
#         m = 0
#         for n in accumulate(sorted(usageLimits)):
#             if n >= (m + 1) * (m + 2) // 2:
#                 m += 1
#         return m

from typing import List

class Solution:
    def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
        usageLimits.sort()
        n = len(usageLimits)

        def canForm(k: int) -> bool:
            available = 0
            # To form k groups of sizes 1, 2, ..., k, 
            # we check if accumulated capacity satisfies required group sizes.
            required_group_size = 1
            
            for limit in usageLimits:
                available += min(limit, k)
                # If we have enough elements to form the current required group size,
                # we fulfill this group and look for the next size.
                if required_group_size <= k and available >= required_group_size * (required_group_size + 1) // 2:
                    required_group_size += 1
            
            return required_group_size > k

        low = 1
        high = n
        ans = 0

        while low <= high:
            mid = (low + high) // 2
            if canForm(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans