# class Solution:
#     def minOperations(self, s: str) -> int:
        
#         res = "".join(sorted(s))
#         n = len(s)

#         if s == res :
#             return 0
        
#         mini , maxi = res[0] , res[1]

#         if mini == s[0] or maxi == s[-1] :
#             return 1
        
#         if n == 2 and s[0] > s[1] :
#             return -1
        
#         if mini == s[-1] and maxi == s[0] and s.count(mini) == 1 and s.count(maxi) == 1 :
#             return 3
        
#         else :
#             return 2

class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        sorted_s = "".join(sorted(s))
        
        # Already sorted
        if s == sorted_s:
            return 0
        
        # Length 2 and not sorted cannot be fixed (proper substring is length 1)
        if n == 2:
            return -1
        
        mn = sorted_s[0]
        mx = sorted_s[-1]
        
        # Minimum character is at index 0 or maximum character is at index n-1
        if s[0] == mn or s[-1] == mx:
            return 1
        
        # Check if mn is at the end and nowhere else, and mx is at the beginning and nowhere else
        if s[0] == mx and s[-1] == mn and s.count(mn) == 1 and s.count(mx) == 1:
            return 3
        
        return 2