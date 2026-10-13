# class Solution:
#     def maxAlternatingSum(self, nums: List[int]) -> int:
        
#         n = len(nums)

#         for i in range(n) :
#             if nums[i] < 0 :
#                 nums[i] = -nums[i]
        
#         nums.sort()

#         if n%2 == 0 :
#             total_left = 0
#             total_right = 0
#             for i in range(n//2) :
#                 total_left += nums[i]**2
#                 total_right += nums[n-i-1]**2
            
#             return total_right-total_left
        

#         else :
#             total_left , total_right = 0 , 0
#             left , right = 0 , n-1

#             while left <= right :
#                 total_left += nums[left]**2
#                 total_right += nums[right]**2
#                 left += 1
#                 right -= 1
            
#             return total_right-total_left



# class Solution:
#     def maxAlternatingSum(self, nums: List[int]) -> int:
        
#         n = len(nums)

#         for i in range(n) :
#             if nums[i] < 0 :
#                 nums[i] = -nums[i]
        
#         nums.sort()

#         if n%2 == 0 :
#             total_left = 0
#             total_right = 0
#             for i in range(n//2) :
#                 total_left += nums[i]**2
#                 total_right += nums[n-i-1]**2
            
#             return total_right-total_left
        

#         else :
#             total_left , total_right = 0 , 0
            
#             # The smaller (n // 2) elements are subtracted
#             for i in range(n // 2):
#                 total_left += nums[i]**2
            
#             # The larger remaining (n // 2 + 1) elements are added
#             for i in range(n // 2, n):
#                 total_right += nums[i]**2
            
#             return total_right-total_left

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # Convert each number to its square and sort
        squares = sorted(x * x for x in nums)
        
        # The smaller n // 2 elements are subtracted
        # The larger remaining elements are added
        k = len(nums) // 2
        return sum(squares[k:]) - sum(squares[:k])