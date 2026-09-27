# class Solution:
#     def longestSubarray(self, nums: list[int], k: int) -> int:
        
#         n = len(nums)

#         @lru_cache(maxsize=None)
#         def dp(indx , total , can_neg , start) :

#             if indx >= n :
#                 if start and total%k == 0 :
#                     return 0
#                 else :
#                     return float("-inf")
            
#             ans = float("-inf")

#             if not start :
#                 # skip this ele
#                 ans = max(ans , dp(indx+1 , 0 , True , False))

#                 # start here
#                 ans = max(ans , 1 + dp(indx+1 , nums[indx]%k , True , True) , 1 + dp(indx+1 , (-nums[indx])%k , False , True))
            
#             else :
#                 #continue
#                 if can_neg : 
#                     ans = max(ans , 1 + dp(indx+1 , (total - nums[indx])%k , False , True) , 1 + dp(indx+1 , total + nums[indx] , True , True))
                
#                 else :
#                     ans = max(ans , 1 + dp(indx+1 , (total + nums[indx])%k , False , True))
                
#                 # end
#                 if total%k == 0 :
#                     ans = max(ans , 0)
            
#             return ans
        
#         res = dp(0 , 0 , True , False)
#         if res == float("-inf") :
#             return 0
#         else :
#             return res

            


# class Solution:
#     def longestSubarray(self, nums: list[int], k: int) -> int:
#         n = len(nums)
#         max_len = 0

#         for i in range(n):
#             current_sum = 0
#             for j in range(i, n):
#                 current_sum += nums[j]
                
#                 # Case 1: Subarray sum is directly divisible by k
#                 if current_sum % k == 0:
#                     max_len = max(max_len, j - i + 1)
#                     continue

#                 # Case 2: Check if negating ANY single element nums[m] in nums[i..j] 
#                 # makes (current_sum - 2 * nums[m]) % k == 0
#                 for m in range(i, j + 1):
#                     if (current_sum - 2 * nums[m]) % k == 0:
#                         max_len = max(max_len, j - i + 1)
#                         break

#         return max_len

class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        n, best = len(nums), 0
        for l in range(n):
            if n - l <= best:
                break
            total, doubled = 0, set()
            for r in range(l, n):
                total += nums[r]
                doubled.add(2 * nums[r] % k)
                if total % k == 0 or total % k in doubled:
                    best = max(best, r - l + 1)
        return best