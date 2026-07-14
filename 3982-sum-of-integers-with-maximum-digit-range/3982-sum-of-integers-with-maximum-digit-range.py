class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        
        n = len(nums)
        digits = defaultdict(int)
        for i in range(n):
            s = str(nums[i])
            maxi , mini = int(max(s)) , int(min(s))
            digits[maxi-mini] += nums[i]
        
        return digits[max(digits)]




