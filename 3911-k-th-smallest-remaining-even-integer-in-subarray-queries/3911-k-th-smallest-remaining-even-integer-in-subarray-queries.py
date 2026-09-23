# class Solution:
#     def kthRemainingInteger(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        
#         n = len(nums)
#         pref = [0]*(n+1)

#         for i in range(n) :
#             prefix[i+1] = pref[i] + (1 if nums[i] % 2 == 0 else 0)
        
#         def count_evens_in_range(left , right) :
#             if left > right :
#                 return 0
            
#             return prefix[right+1] - prefix[left]
        
#         ans = []

#         for left , right , k in queries :

#             low = 2
#             high = 2*k + 2*(right-left+1)
#             res = high

#             while low <= high :
#                 mid = (low + high)//2

#                 if mid % 2 != 0 :
#                     mid -= 1
                
#                 if mid < low :
#                     break
                
#                 total_evens = mid//2
#                 # nums[left , right] <= mid
#                 indx = bisect.bisect_right(nums , mid , left , right+1) - 1

#                 removed_evens = count_evens_in_range(left , indx)

#                 left_evens = total_evens - removed_evens

#                 if left_evens >= k :
#                     res = mid
#                     high = mid - 2
#                 else :
#                     low = mid+2
            
#             ans.append(res)
        
#         return ans

import bisect

class Solution:
    def kthRemainingInteger(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        n = len(nums)
        
        # Precompute prefix count of even numbers in nums
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + (1 if nums[i] % 2 == 0 else 0)
            
        def count_evens_in_range(l: int, r: int) -> int:
            """Returns count of even numbers in subarray nums[l..r]"""
            if l > r:
                return 0
            return pref[r + 1] - pref[l]

        ans = []
        for l, r, k in queries:
            # Binary search for the smallest even integer X
            low = 2
            high = 2 * k + 2 * (r - l + 1)
            res = high

            while low <= high:
                mid = (low + high) // 2
                # Ensure mid is even
                if mid % 2 != 0:
                    mid -= 1

                if mid < low:
                    break

                # Count total even numbers <= mid
                total_evens = mid // 2

                # Find how many elements in nums[l..r] are <= mid
                # bisect_right finds the rightmost index in nums with value <= mid
                idx = bisect.bisect_right(nums, mid, l, r + 1) - 1
                
                # Count even numbers in nums[l..idx]
                removed_evens = count_evens_in_range(l, idx)

                remaining_evens = total_evens - removed_evens

                if remaining_evens >= k:
                    res = mid
                    high = mid - 2  # Try searching for a smaller even integer
                else:
                    low = mid + 2   # Need a larger even integer

            ans.append(res)

        return ans