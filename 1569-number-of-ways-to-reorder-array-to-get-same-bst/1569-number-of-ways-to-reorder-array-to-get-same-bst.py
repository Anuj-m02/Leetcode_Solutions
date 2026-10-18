from collections import defaultdict , deque , Counter
import math

class Solution:
    def numOfWays(self, nums: List[int]) -> int:

        n = len(nums)
        root = nums[0]
        mod = int(1e9)+7

        def dfs(arr) :
            if len(arr) <= 2 :
                return 1
            
            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]

            ways = math.comb(len(left) + len(right) , len(left))%mod

            return ways * (dfs(left)*dfs(right))%mod
        
        return (dfs(nums) - 1)%mod


        