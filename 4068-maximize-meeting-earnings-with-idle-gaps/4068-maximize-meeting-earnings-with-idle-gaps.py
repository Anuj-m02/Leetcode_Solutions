class Solution:
    def maxEarnings(self, meetings: list[list[int]]) -> int:
        
        # sort on start time
        meetings.sort()
        n = len(meetings)

        starts = [m[0] for m in meetings]

        @lru_cache(maxsize=None)
        def dp(indx) :
            if indx >= n :
                return 0
            
            # skip curr meeting
            res = dp(indx+1)

            # pick this meeintg
            start , end , rev = meetings[indx]
            nxt = bisect.bisect_left(starts , end)

            take = max(rev + start ,  rev + start - end + dp(nxt))

            return max(take , res)
        
        
        ans = 0
        for indx in range(n) :
            start , end , rev = meetings[indx]
            nxt = bisect.bisect_left(starts , end)
            # If meetings[i] is the first meeting chosen:
            # Only meeting: rev
            # Followed by others: (rev - end) + dp(nxt)

            ans = max(ans , rev , rev - end + dp(nxt))
        
        return ans