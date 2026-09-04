# class Solution:
#     def checkPartitioning(self, s: str) -> bool:
        
#         n = len(s)

#         def check(string) :

#             return string == string[::-1] 

#         @lru_cache(maxsize=None)
#         def dp(indx1) :
        
#             if indx1 >= n :
#                 return False

#             for i in range(indx1+1 , n) :

#                 candid_1  , candid_2 , candid_3 = s[:indx1] , s[indx1 : i] , s[i : n]

#                 if check(candid_1) and check(candid_2) and check(candid_3) :
#                     return True
                
            
#             return dp(indx1 + 1)
        
#         return dp(1)
            


from functools import lru_cache

class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        
        # Precalculate palindrome table: is_pal[i][j] is True if s[i:j] is a palindrome
        is_pal = [[False] * (n + 1) for _ in range(n + 1)]
        
        for length in range(1, n + 1):
            for start in range(n - length + 1):
                end = start + length
                if length == 1:
                    is_pal[start][end] = True
                elif length == 2:
                    is_pal[start][end] = (s[start] == s[start + 1])
                else:
                    is_pal[start][end] = (s[start] == s[end - 1]) and is_pal[start + 1][end - 1]

        @lru_cache(maxsize=None)
        def dp(indx1):
            # candid_1 is s[0:indx1], so indx1 must be at least 1 (non-empty first part)
            if indx1 >= n - 1:
                return False

            # Ensure candid_1 is valid
            if not is_pal[0][indx1]:
                return dp(indx1 + 1)

            # Check candid_2 (s[indx1:i]) and candid_3 (s[i:n])
            # i must be > indx1 so candid_2 is non-empty, and i < n so candid_3 is non-empty
            for i in range(indx1 + 1, n):
                if is_pal[indx1][i] and is_pal[i][n]:
                    return True

            return dp(indx1 + 1)

        return dp(1)