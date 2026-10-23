class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        
        n = len(nums)

        maxi = -1

        for i in range(n) :
            for j in range(n) :
                if i == j :
                    continue
                maxi = max(maxi , (nums[i]-1)*(nums[j]-1))
        
        return maxi