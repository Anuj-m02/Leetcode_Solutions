class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def atmost(goal: int) -> int:
            if goal < 0:
                return 0

            left = 0
            cnt = 0
            ans = 0

            for right in range(n):
                if nums[right] % 2 == 1:
                    cnt += 1

                while cnt > goal:
                    if nums[left] % 2 == 1:
                        cnt -= 1
                    left += 1

                # Every subarray ending at 'right' starting from 'left' to 'right' has <= goal odd numbers
                ans += right - left + 1

            return ans

        return atmost(k) - atmost(k - 1)