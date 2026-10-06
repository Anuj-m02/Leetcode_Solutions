# class Solution:
#     def minMaxSums(self, nums: List[int], k: int) -> int:
        
#         nums.sort()
#         n = len(nums)
#         mod = int(1e9) + 7

#         # start indx 0 - n-k
#         # end indx = start_indx + k
#         # since arr sorted we know min and max min is start indx and max is end indx

#         @lru_cache(maxsize=None)
#         def count_subsets(indx , cnt) :

#             if cnt == k or indx >= n :
#                 return 0
            
#             not_pick = count_subsets(indx + 1 , cnt)

#             pick = 1 + count_subs(indx + 1, cnt+1)

#             return (pick + not_pick)%mod
        
        
#         total_sum = 0

#         for indx in range(n) :

#             subsets_with_min = 1 + count_subsets(indx + 1  , 1)

#             subsets_with_max = 1 + count_subsets(n-indx , 1)

#             total_contribution = (subsets_with_min + subsets_with_max)*(nums[indx]) % mod
#             total_sum += total_contribution % mod
        
#         return total_sum % mod





class Solution:
    def minMaxSums(self, nums: List[int], k: int) -> int:
        nums.sort()
        total_sums = 0
        quantity = 1
        
        for i in range(len(nums)):
            total_sums += quantity * (nums[i] + nums[-i - 1])
            quantity = 2 * quantity - comb(i, k - 1)

        return total_sums % (10 ** 9 + 7)