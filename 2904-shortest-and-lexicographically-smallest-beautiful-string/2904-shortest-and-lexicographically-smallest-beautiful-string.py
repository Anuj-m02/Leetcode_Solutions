# class Solution:
#     def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        
#         n = len(s)

#         left , right = 0 , 0
#         cnt = 0

#         ans = "1"*101
#         mini = float("inf")



#         for right in range(n) :

#             if s[right] == "1" :
#                 cnt += 1
            
#             # while cnt > k :
#             #     if s[left] == "1" :
#             #         cnt -= 1
#             #     left += 1
            
#             while cnt == k and left <= right :
#                 if s[left] == "1" :
#                     length = right-left+1
#                     sub = s[left:right+1]

#                     if length < mini :
#                         mini = length
#                         ans = sub
#                     elif length == mini :
#                         ans = min(ans , sub)
                    
#                     cnt -= 1
                
#                 left += 1


        
#         if ans == "1"*101 :
#             return ""
        
#         else :
#             return ans

class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        left = 0
        cnt = 0
        
        ans = "1" * 101
        mini = float("inf")

        for right in range(n):
            if s[right] == "1":
                cnt += 1
            
            # Shrink if we have excess ones
            while cnt > k:
                if s[left] == "1":
                    cnt -= 1
                left += 1
            
            # Trim leading zeros to minimize length
            while cnt == k and s[left] == "0":
                left += 1
            
            # Record valid candidate substring starting with '1'
            if cnt == k:
                length = right - left + 1
                sub = s[left : right + 1]
                
                if length < mini:
                    mini = length
                    ans = sub
                elif length == mini:
                    ans = min(ans, sub)

        return "" if ans == "1" * 101 else ans


