# class Solution:
#     def maxEarnings(self, meetings: list[list[int]]) -> int:
        
#         # sort on start time
#         meetings.sort()
#         n = len(meetings)

#         starts = [m[0] for m in meetings]

#         @lru_cache(maxsize=None)
#         def dp(indx) :
#             if indx >= n :
#                 return 0
            
#             # skip curr meeting
#             res = dp(indx+1)

#             # pick this meeintg
#             start , end , rev = meetings[indx]
#             nxt = bisect.bisect_left(starts , end)

#             take = max(rev + start ,  rev + start - end + dp(nxt))

#             return max(take , res)
        
        
#         ans = 0
#         for indx in range(n) :
#             start , end , rev = meetings[indx]
#             nxt = bisect.bisect_left(starts , end)
#             # If meetings[i] is the first meeting chosen:
#             # Only meeting: rev
#             # Followed by others: (rev - end) + dp(nxt)

#             ans = max(ans , rev , rev - end + dp(nxt))
        
#         return ans
import bisect
from functools import cache

class Solution:
    def maxEarnings(self, meetings: list[list[int]]) -> int:
        # Sort meetings by start time
        meetings.sort()
        n = len(meetings)
        starts = [m[0] for m in meetings]

        @cache
        def dp(i: int, is_first: bool) -> int:
            """
            dp(i, True)  -> Max profit considering meetings from index i onwards, 
                            where NO meeting has been chosen yet (i.e. next chosen meeting is FIRST).
            dp(i, False) -> Max profit considering meetings from index i onwards, 
                            where AT LEAST ONE meeting has already been chosen before.
            """
            if i >= n:
                return 0

            # Option 1: Skip meeting i
            ans = dp(i + 1, is_first)

            start, end, revenue = meetings[i]
            nxt = bisect.bisect_left(starts, end)

            # Option 2: Pick meeting i
            if is_first:
                # If meeting i is the VERY FIRST meeting selected in the sequence:
                # - If it's also the ONLY meeting: earn `revenue`
                # - If more meetings follow: earn `(revenue - end) + dp(nxt, False)`
                take_only = revenue
                take_more = (revenue - end) + dp(nxt, False)
                ans = max(ans, take_only, take_more)
            else:
                # If meeting i is NOT the first meeting (i.e., previous meetings exist):
                # - If it's the LAST meeting: earn `revenue + start`
                # - If more meetings follow: earn `(revenue + start - end) + dp(nxt, False)`
                take_last = revenue + start
                take_more = (revenue + start - end) + dp(nxt, False)
                ans = max(ans, take_last, take_more)

            return ans

        # Single entry point starting from index 0 where no meeting has been chosen yet
        return dp(0, True)