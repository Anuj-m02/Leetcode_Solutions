class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        m, n = len(nums1), len(nums2)
        total_len = m + n
        
        # Target index for odd, or the second middle index for even
        mid_index = total_len // 2
        
        i = j = 0
        prev = curr = 0
        
        # Iterate up to the middle index
        for count in range(mid_index + 1):
            prev = curr
            
            # Pick the smaller element from nums1 or nums2
            if i < m and (j >= n or nums1[i] <= nums2[j]):
                curr = nums1[i]
                i += 1
            else:
                curr = nums2[j]
                j += 1
                
        # If total length is odd, return curr
        if total_len % 2 != 0:
            return float(curr)
        # If even, return the average of the two middle values
        else:
            return (prev + curr) / 2.0