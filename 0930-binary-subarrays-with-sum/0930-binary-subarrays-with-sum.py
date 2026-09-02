# class Solution:
#     def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

#         class Solution:
#     def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
#         curr = 0
#         cnt = 0
#         prefix_cnts = defaultdict(int)
#         prefix_cnts[0] = 1
        
#         for num in nums:
#             curr += num
#             cnt += prefix_cnts[curr - goal]
#             prefix_cnts[curr] += 1
            
#         return cnt

        
#         n = len(nums)

#         left , right , res , total = 0 , 0 ,0 ,0
#         for right in range(n) :

#             total += nums[right]

#             while total > goal :
#                 total -= nums[left]
#                 left +=1
            
#             if total == goal :
#                 res += right-left+1
        
#         return res

#         # curr = 0
#         # cnt = 0
#         # prefix_cnts = defaultdict(int)
#         # prefix_cnts[0] = 1
#         # for num in nums :
#         #     curr += num
#         #     cnt += prefix_cnts[curr-goal]
#         #     prefix_cnts[curr] += 1
#         # return cnt
            
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def numSubarraysWithAtMost(k: int) -> int:
            if k < 0:
                return 0
            
            left = 0
            total_sum = 0
            count = 0
            
            for right in range(len(nums)):
                total_sum += nums[right]
                
                # Shrink window until total_sum <= k
                while total_sum > k:
                    total_sum -= nums[left]
                    left += 1
                
                # All subarrays ending at 'right' starting from 'left' up to 'right' are valid
                count += right - left + 1
                
            return count

        return numSubarraysWithAtMost(goal) - numSubarraysWithAtMost(goal - 1)