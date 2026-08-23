# class Solution:
#     def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
#         n = len(mat)
#         m = len(mat[0])
#         low = 0
#         high = m-1
#         while low<=high:
#             mid = (low+high)//2
#             max_row = 0
#             for i in range(1, n):
#                 if mat[i][mid] > mat[max_row][mid]:
#                     max_row = i
#             # maxrow = max(range(n),key=lambda r :mat[r][mid])

#             curr = mat[max_row][mid]

#             maxi = mat[max_row][mid]

#             if mid > 0 :
#                 left = mat[max_row][mid-1]
#             else :
#                 left = -1
#             if mid < m-1 :
#                 right  = mat[max_row][mid+1]
#             else :
#                 right = -1
#             if maxi > left and maxi > right :
#                 return [max_row,mid]
#             if maxi < left :
#                 high = mid-1
#             else :
#                 low = mid + 1

#         return [-1,-1]

from typing import List

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        low = 0
        high = m - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            # 1. Find the row containing the maximum element *only* in the 'mid' column
            max_row = 0
            for i in range(1, n):
                if mat[i][mid] > mat[max_row][mid]:
                    max_row = i
            
            # 2. Extract values for current, left, and right neighbors safely
            maxi = mat[max_row][mid]
            left = mat[max_row][mid - 1] if mid > 0 else -1
            right = mat[max_row][mid + 1] if mid < m - 1 else -1
            
            # 3. Check if the current element is a peak
            if maxi > left and maxi > right:
                return [max_row, mid]
            
            # 4. Narrow down boundaries safely
            if maxi < left:
                high = mid - 1
            else:
                low = mid + 1
                
        return [-1, -1]
