# class Solution:
#     def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:

#         n = len(num1)
#         k = k1+k2

#         diffs = [abs(nums1[i] - nums2[i]) for i in range(n)]
#         max_diff = max(diffs)

#         if max_diff == 0 or k == 0 :
#             return sum(d*d for d in diffs)
        
#         count = [0]*(max_diff + 1)
#         for d in diffs :
#             count[d] += 1
        
#         for d in range(max_diff , 0 , -1) :
#             if count[d] == 0 :
#                 continue
            
#             if k >= count[d] :
#                 k -= count[d]
#                 count[d-1] += count[d]
#                 count[d] = 0
            
#             else :
#                 count[d-1] += k
#                 count[d] -= k
#                 k = 0
#                 break
        
#         return sum(d*d*count[d] for d in range(max_diff+1))
class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        n = len(nums1)
        k = k1 + k2
        
        # Calculate absolute differences
        diffs = [abs(nums1[i] - nums2[i]) for i in range(n)]
        max_diff = max(diffs)
        
        if max_diff == 0 or k == 0:
            return sum(d * d for d in diffs)
        
        # Frequency array for differences (up to max_diff)
        count = [0] * (max_diff + 1)
        for d in diffs:
            count[d] += 1
            
        # Reduce differences greedily from the largest down to 1
        for d in range(max_diff, 0, -1):
            if count[d] == 0:
                continue
            
            if k >= count[d]:
                # We can reduce all elements of value 'd' down to 'd - 1'
                k -= count[d]
                count[d - 1] += count[d]
                count[d] = 0
            else:
                # We can only reduce 'k' elements of value 'd' down to 'd - 1'
                count[d - 1] += k
                count[d] -= k
                k = 0
                break
                
        # Calculate final sum of squared differences
        return sum(d * d * count[d] for d in range(max_diff + 1))