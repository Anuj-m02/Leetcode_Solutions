class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        
        n , m = len(nums) , len(multipliers)


        @cache
        def dp(indx , left) :

            if indx >= m :
                return 0
            

            right = n-1-(indx-left)

            pick_left = nums[left]*multipliers[indx] + dp(indx+1 , left+1)

            pick_right = nums[right]*multipliers[indx] + dp(indx+1 , left)

            return max(pick_left , pick_right)
            

        
        return dp(0 , 0)