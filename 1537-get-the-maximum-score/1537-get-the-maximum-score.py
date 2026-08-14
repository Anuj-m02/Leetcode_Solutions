from collections import defaultdict , deque , Counter
import heapq
from functools import lru_cache


class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:

        n , m = len(nums1) , len(nums2)

        p1 , p2 , sum1 , sum2 , ans = 0 , 0 , 0 , 0 , 0

        while p1 < n and p2 < m :

            if nums1[p1] == nums2[p2] :
                ans += max(sum1 , sum2) + nums1[p1]
                sum1 , sum2 = 0, 0
                p1 , p2 = p1+1 , p2+1
            
            elif nums1[p1] < nums2[p2] :
                sum1 += nums1[p1]
                p1 += 1
            
            else :
                sum2 += nums2[p2]
                p2 += 1
        
        while (p1 < n) :
            sum1 += nums1[p1]
            p1 += 1
        
        while (p2 < m) :
            sum2 += nums2[p2]
            p2 += 1
        
        return (ans + max(sum1 , sum2)) % (10**9 + 7)
