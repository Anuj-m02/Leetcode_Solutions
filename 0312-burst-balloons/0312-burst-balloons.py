class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}
        def recursion(i,j,dp):
            if i == j :
                return 0
            if (i,j) in dp :
                return dp[(i,j)]
            maxi = float('-inf')
            for k in range(i,j):
                curr_cost = nums[i-1]*nums[k]*nums[j]
                left_cost = recursion(i,k,dp)
                right_cost = recursion(k+1,j,dp)
                maxi = max(maxi , curr_cost + left_cost + right_cost)
            dp[(i,j)] = maxi
            return maxi
        return recursion(1,len(nums)-1, dp)