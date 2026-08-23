from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low , high = 0 , n-1

        while low <= high :
            mid = low + (high-low)//2

            if nums[mid] == target :
                return mid
            
            if nums[low] <= nums[mid] :
                if nums[low] <= target <= nums[mid] :
                    high = mid-1
                else :
                    low = mid+1
                
            else :
                if nums[mid] <= target <= nums[high] :
                    low = mid+1
                else :
                    high = mid-1
        
        return -1

        # l, h = 0, n - 1
        
        # while l <= h:
        #     m = l + (h - l) // 2
            
        #     # If the target is found at mid, return the index
        #     if nums[m] == target:
        #         return m
            
        #     # Check which part of the array is sorted
        #     if nums[l] <= nums[m]:
        #         # If the left part is sorted
        #         if nums[l] <= target < nums[m]:
        #             h = m - 1
        #         else:
        #             l = m + 1
        #     else:
        #         # If the right part is sorted
        #         if nums[m] < target <= nums[h]:
        #             l = m + 1
        #         else:
        #             h = m - 1
        
        # return -1
