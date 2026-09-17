class Solution:
    def wiggleMaxLength(self, nums: list[int]) -> int:
        
        n = len(nums)

        @lru_cache(maxsize=None)
        def dp(indx , prev_num , prev_parity) :
            if indx >= n :
                return 0
            
            # option 1 we can skip this num
            op1 = dp(indx+1 , prev_num , prev_parity)

            op2 = 0
            # we can pick if its alterantte
            curr_num = nums[indx]
            if prev_num is None :
                op2 = 1 + dp(indx+1 , curr_num , -1)
            elif curr_num > prev_num and (prev_parity == 0 or prev_parity == -1) :
                op2 += 1 + dp(indx+1 , curr_num , 1)
            elif curr_num < prev_num and (prev_parity == 1 or prev_parity == -1) :
                op2 += 1 + dp(indx+1 , curr_num , 0)           

            return max(op1 , op2)
        
        return dp(0 , None ,-1)


