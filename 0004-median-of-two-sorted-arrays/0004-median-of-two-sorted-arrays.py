class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # Ensure nums1 is the smaller array to optimize binary search range
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        low, high = 0, m
        half_len = (m + n + 1) // 2

        while low <= high:
            i = (low + high) // 2
            j = half_len - i

            # Edge cases: handle partitions at boundaries using infinity
            max_left1 = float("-inf") if i == 0 else nums1[i - 1]
            min_right1 = float("inf") if i == m else nums1[i]

            max_left2 = float("-inf") if j == 0 else nums2[j - 1]
            min_right2 = float("inf") if j == n else nums2[j]

            # Check if correct partition is found
            if max_left1 <= min_right2 and max_left2 <= min_right1:
                # Odd combined length: median is the maximum of left elements
                if (m + n) % 2 != 0:
                    return float(max(max_left1, max_left2))
                # Even combined length: average of max left and min right
                return (
                    max(max_left1, max_left2) + min(min_right1, min_right2)
                ) / 2.0

            elif max_left1 > min_right2:
                high = i - 1  # Partition in nums1 is too far right
            else:
                low = i + 1  # Partition in nums1 is too far left

        # m, n = len(nums1), len(nums2)
        # total_len = m + n
        
        # # Target index for odd, or the second middle index for even
        # mid_index = total_len // 2
        
        # i = j = 0
        # prev = curr = 0
        
        # # Iterate up to the middle index
        # for count in range(mid_index + 1):
        #     prev = curr
            
        #     # Pick the smaller element from nums1 or nums2
        #     if i < m and (j <= n or nums1[i] <= nums2[j]):
        #         curr = nums1[i]
        #         i += 1
        #     else:
        #         curr = nums2[j]
        #         j += 1
                
        # # If total length is odd, return curr
        # if total_len % 2 != 0:
        #     return float(curr)
        # # If even, return the average of the two middle values
        # else:
        #     return (prev + curr) / 2.0