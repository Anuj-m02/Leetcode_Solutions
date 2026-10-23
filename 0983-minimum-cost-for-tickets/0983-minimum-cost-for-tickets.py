class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        
        n = len(days)

        days.sort()

        @lru_cache(maxsize=None)
        def dp(indx) :

            if indx >= n :
                return 0
            
            curr_day = days[indx]
            nxt_indx = bisect.bisect_left(days , curr_day+7)
            nxt_indx1 = bisect.bisect_left(days , curr_day+30)
            op1 = costs[0] + dp(indx+1)
            op2 = costs[1] + dp(nxt_indx)
            op3 = costs[2] + dp(nxt_indx1)

            return min(op1 , op2 , op3)
        
        return dp(0)
    
