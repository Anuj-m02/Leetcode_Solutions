# class Solution:
#     def combinationSum(self, arr: List[int], target: int) -> List[List[int]]:
#         res = []
#         ds = []
#         def f(indx,target,arr,res,ds):
#             if indx == len(arr):
#                 if target == 0 :
#                     res.append(ds.copy())
#                 return 
#             if arr[indx] <= target :
#                 ds.append(arr[indx])
#                 f(indx,target-arr[indx],arr,res,ds)
#                 ds.pop()
#             f(indx+1,target,arr,res,ds)
#         f(0,target,arr,res,ds)
#         return res

from typing import List

class Solution:
    def combinationSum(self, arr: List[int], target: int) -> List[List[int]]:
        memo = {}

        def f(indx: int, target: int) -> List[List[int]]:
            # Base Cases
            if target == 0:
                return [[]]  # One valid combination: the empty set
            if indx == len(arr) or target < 0:
                return []    # No valid combination possible

            # Return memoized result if available
            if (indx, target) in memo:
                return memo[(indx, target)]

            res = []

            # Option 1: Pick the current element (if valid)
            if arr[indx] <= target:
                for sub_comb in f(indx, target - arr[indx]):
                    res.append([arr[indx]] + sub_comb)

            # Option 2: Skip the current element and move to the next
            for sub_comb in f(indx + 1, target):
                res.append(sub_comb)

            # Save result in memo table
            memo[(indx, target)] = res
            return res

        return f(0, target)