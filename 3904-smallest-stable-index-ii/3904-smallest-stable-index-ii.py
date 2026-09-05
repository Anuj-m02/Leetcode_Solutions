class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        # Build suffix_min array
        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])
        
        # Traverse from left to right, maintaining running prefix_max
        prefix_max = nums[0]
        for i in range(n):
            prefix_max = max(prefix_max, nums[i])
            score = prefix_max - suffix_min[i]
            if score <= k:
                return i
                
        return -1