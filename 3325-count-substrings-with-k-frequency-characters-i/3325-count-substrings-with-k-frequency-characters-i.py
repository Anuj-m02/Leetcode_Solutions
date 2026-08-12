# from collections import defaultdict , deque ,Counter
# import heapq
# from functools import lru_cache

# class Solution:
#     def numberOfSubstrings(self, s: str, k: int) -> int:

#         n = len(s)
#         d = defaultdict(int)
#         left , right = 0 , 0
#         cnt = 0

#         def check(d) :

#             for key in d:
#                 if d[key] >= k :
#                     return True
#             return False

#         while right < n :

#             curr_char = s[right]

#             d[curr_char] += 1
            
#             while check(d) :
#                 cnt += (n-right)
#                 temp = s[left]
#                 d[temp] -= 1
#                 left += 1
            
#             right += 1
        
#         return cnt


from collections import defaultdict

class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        d = defaultdict(int)
        left = 0
        cnt = 0
        
        # Track how many distinct characters currently have freq >= k
        at_least_k = 0

        for right in range(n):
            curr_char = s[right]
            d[curr_char] += 1
            
            # If this character just reached frequency k, increment our valid count
            if d[curr_char] == k:
                at_least_k += 1

            # While the current window s[left...right] is valid
            while at_least_k > 0:
                # All substrings from `right` to `n-1` starting at `left` are valid
                cnt += (n - right)
                
                # Shrink the window from the left
                left_char = s[left]
                if d[left_char] == k:
                    at_least_k -= 1
                d[left_char] -= 1
                left += 1

        return cnt