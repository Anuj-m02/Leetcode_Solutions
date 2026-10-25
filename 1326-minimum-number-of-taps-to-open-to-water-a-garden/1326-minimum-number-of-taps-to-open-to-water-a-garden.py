# class Solution:
#     def minTaps(self, n: int, ranges: list[int]) -> int:
        
#         m = len(ranges)
#         intervals = []
#         for i in range(m) :
#             left , right = i - ranges[i] , i + ranges[i]
#             intervals.append((left , right))
        
#         intervals.sort()

#         @lru_cache(maxsize=None)
#         def dp(indx , tap) :

#             if indx >= n :
#                 return 0

#             if tap >= m :
#                 return float("inf")
            
#             ans = float("inf")

#             curr_left , curr_right = intervals[tap]
#             # skip dont place tap here
#             ans =  min(ans , dp(indx , tap+1))

#             # take this tap here
#             if curr_left <= indx :
#                 ans = min(ans , 1 + dp(max(indx , curr_right) , tap+1))

#             return ans
        
#         res = dp(0,0)
#         return res if res != float("inf") else -1


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        max_range = [0] * (n + 1)
        
        for i in range(len(ranges)):
            left = max(0, i - ranges[i])
            right = min(n, i + ranges[i])
            max_range[left] = max(max_range[left], right)
        
        end = farthest = taps = 0
        i = 0
        
        while end < n:
            while i <= end:
                farthest = max(farthest, max_range[i])
                i += 1
            
            if farthest <= end:
                return -1  # Unable to cover the entire garden
            
            end = farthest
            taps += 1
        
        return taps        