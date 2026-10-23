# class Solution:
#     def minimumChanges(self, s: str, k: int) -> int:

#         n = len(s)

#         def help(string) :
#             l = len(string)

#             if l < 2 :
#                 return float("inf")
            
#             min_changes = float("inf")

#             for d in range(1 , l) :
#                 if l%d == 0 :
#                     changes = 0
#                     for g in range(d) :
#                         left = g
#                         right = l-d+g
#                         while left < right :
#                             if string[left] != string[right] :
#                                 changes += 1
                            
#                             left += d
#                             right -= d
                    
#                     min_changes = min(min_changes , changes)
                
#             return min_changes


#         cost = [[0]*n for _ in range(n)]
#         for i in range(n) :
#             for j in range(i+1 , n) :
#                 cost[i][j] = help(s[i:j+1])

#         @lru_cache(maxsize=None)
#         def dp(indx , k_left):

#             if k_left == 0 :
#                 return 0 if indx == n else float("inf")
            
#             if indx >= n :
#                 return float("inf")
            
#             ans = float("inf")

#             max_j = n-2*(k_left-1)-1

#             for j in range(indx+1 , max_j + 1) :
#                 ans = min(ans , cost[i][j] + dp(j+1 , k_left-1))
            
#             return ans
        
#         return dp(0 , k)



from functools import lru_cache

class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        
        # Helper function to compute minimum changes needed to make s[i..j] a semi-palindrome
        def get_min_changes(sub: str) -> int:
            L = len(sub)
            if L < 2:
                return float('inf')
            
            min_changes = float('inf')
            
            # Try all proper divisors d of L (1 <= d < L)
            for d in range(1, L):
                if L % d == 0:
                    changes = 0
                    # Check each of the d groups
                    for g in range(d):
                        # Group g consists of sub[g], sub[g+d], sub[g+2d], ...
                        # Standard 2-pointer palindrome check within the group
                        left = g
                        right = L - d + g
                        while left < right:
                            if sub[left] != sub[right]:
                                changes += 1
                            left += d
                            right -= d
                    min_changes = min(min_changes, changes)
                    
            return min_changes

        # Precompute cost[i][j] for all valid substrings s[i..j]
        cost = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):  # Substrings must have length >= 2
                cost[i][j] = get_min_changes(s[i:j+1])

        # Top-down DP with Memoization
        @lru_cache(None)
        def dp(i: int, k_left: int) -> int:
            # Base Cases
            if k_left == 0:
                return 0 if i == n else float('inf')
            if i >= n:
                return float('inf')

            ans = float('inf')
            
            # Choose the end of the current partition: j
            # Substring s[i..j] has length (j - i + 1) >= 2
            # Remaining suffix s[j+1..n-1] must have length >= 2 * (k_left - 1)
            max_j = n - 2 * (k_left - 1) - 1
            
            for j in range(i + 1, max_j + 1):
                ans = min(ans, cost[i][j] + dp(j + 1, k_left - 1))

            return ans

        return dp(0, k)