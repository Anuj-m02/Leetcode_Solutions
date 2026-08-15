from functools import lru_cache
class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:

        n = len(nums)
        a = 0
        for i in range(n) :
            a = a^nums[i]
        
        cnt = nums.count(0)
        if cnt == n :
            return 0
        
        if a != 0 :
            return n
        else :
            return n-1

        # @lru_cache(maxsize=None)
        # def dp(indx , cnt , prev_xor) :
        #     if indx == n :
        #         if prev_xor == 0 :
        #             return cnt
        #         else :
        #             return 0            
        #     # each indx we have toption whether to xor or not

        #     opt1 = dp(indx+1 , cnt , prev_xor)

        #     curr_char = nums[indx]
        #     new_xor = prev_xor ^ curr_char
        #     opt2 = dp(indx+1 , cnt+1 , new_xor)

        #     return max(opt1 , opt2)
        
        # return dp(0 , 0 , 0)



