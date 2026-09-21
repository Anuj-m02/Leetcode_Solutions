# class Solution:
#     def countGoodSubstrings(self, s: str) -> int:
        
#         n = len(s)
#         cnt = 0 

#         left , right = 0 , 0

#         for right in range(n) :
#             curr_start , curr_end = right , right + 3

#             if curr_end > n-1 :
#                 break
            
#             substring = s[curr_start : curr_end]
#             if substring[0] != substring[1] and substring[1] != substring[2] and substring[0] != substring[2] :
#                 cnt += 1
        
#         return cnt

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n = len(s)
        cnt = 0 

        left , right = 0 , 0

        for right in range(n) :
            curr_start , curr_end = right , right + 3

            if curr_end > n :
                break
            
            substring = s[curr_start : curr_end]
            if substring[0] != substring[1] and substring[1] != substring[2] and substring[0] != substring[2] :
                cnt += 1
        
        return cnt