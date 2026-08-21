class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        
        n = len(nums)

        @lru_cache(maxsize=None)
        def dp(curr_indx , is_even) :

            if curr_indx == n :
                if is_even :
                    return 0
                else :
                    return float("-inf")
            
            no_xor = nums[curr_indx] + dp(curr_indx+1 , is_even)
            with_xor = (nums[curr_indx] ^ k) + dp(curr_indx+1 , not is_even)

            maxi = max(no_xor , with_xor)
            return maxi
        
        return dp(0 , 1)