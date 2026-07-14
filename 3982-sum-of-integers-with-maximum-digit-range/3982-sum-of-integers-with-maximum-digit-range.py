# class Solution:
#     def maxDigitRange(self, nums: list[int]) -> int:
        
#         n = len(nums)
#         digits = defaultdict(int)
#         for i in range(n):
#             s = str(nums[i])
#             maxi , mini = int(max(s)) , int(min(s))
#             digits[maxi-mini] += nums[i]
        
#         return digits[max(digits)]



class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:

        best = -1
        ans = 0

        for num in nums:
            s = str(num)
            diff = int(max(s)) - int(min(s))

            if diff > best:
                best = diff
                ans = num
            elif diff == best:
                ans += num

        return ans
