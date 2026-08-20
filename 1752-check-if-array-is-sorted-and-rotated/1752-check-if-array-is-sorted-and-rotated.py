# class Solution:
#     def check(self, nums: List[int]) -> bool:
#         n = len(nums)
#         if nums == sorted(nums):
#             return True
#         count = 0
#         indx = -1
#         for i in range(1,n):
#             if nums[i] > nums[i-1] and count < 2:
#                 continue
#             elif nums[i] < nums[i-1] and count < 1 :
#                 count += 1
#                 indx = i
#             elif nums[i] > nums[i-1] and count > 1 :
#                 return False
#             elif nums[i] < nums[i-1] and count > 1 :
#                 return False
#         temp = nums[indx:] + nums[:indx]
#         if temp == sorted(nums):
#             return True
#         else :
#             return False

class Solution:

  def check(self, nums: list[int]) -> bool:
    count = 0
    n = len(nums)
    for i in range(n):
      if nums[i] > nums[(i + 1) % n]:
        count += 1
    return count <= 1