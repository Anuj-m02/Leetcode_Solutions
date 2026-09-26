# class Solution:
#     def perfectPairs(self, nums: List[int]) -> int:
        
#         arr = sorted(abs(x) for x in nums)
#         n = len(arr)
#         res = 0
#         left = 0

#         for right in range(n):

#             # left = max(left , right+1)
#             while left < n and arr[left] <= 2*arr[right] :
#                 left += 1
            
#             res += (right-left+1)
        
#         return res

class Solution:
    def perfectPairs(self, nums: list[int]) -> int:
        A = sorted(abs(x) for x in nums)
        n = len(A)
        res = 0
        j = 0
        
        for i in range(n):
            j = max(j, i + 1)
            while j < n and A[j] <= 2 * A[i]:
                j += 1
            res += (j - i - 1)
            
        return res