class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        
        # Check if nums is an increasing cyclic shift
        is_increasing = True
        # Check if nums is a decreasing cyclic shift
        is_decreasing = True
        
        for i in range(n):
            if nums[(i + 1) % n] != (nums[i] + 1) % n:
                is_increasing = False
            if nums[(i + 1) % n] != (nums[i] - 1 + n) % n:
                is_decreasing = False

        if not is_increasing and not is_decreasing:
            return -1
        
        idx = nums.index(0)
        
        ans = float('inf')
        
        if is_increasing:
            # Option 1: Rotate left `idx` times
            cost1 = idx
            # Option 2: Reverse, rotate left `n - idx` times, reverse again
            cost2 = (n - idx) + 2
            ans = min(ans, cost1, cost2)
            
        if is_decreasing:
            # Option 1: Reverse first, then rotate
            cost1 = n - idx
            # Option 2: Rotate first, then reverse
            cost2 = idx + 2
            ans = min(ans, cost1, cost2)
            
        return ans