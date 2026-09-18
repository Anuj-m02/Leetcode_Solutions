class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:

        n = len(startTime)

        schedule = []
        for indx in range(n) :
            schedule.append((startTime[indx] , endTime[indx] , profit[indx]))
        
        arr = sorted(schedule)

        starts = [job[0] for job in arr]


        @lru_cache(maxsize=None)
        def dp(indx) :
            if indx >= n :
                return 0
            
            # skip this indx
            op1 = dp(indx+1)

            # take this indx only if curr_Start >= prev_end
            curr_start , curr_end , curr_profit = arr[indx]
            nxt_indx = bisect.bisect_left(starts , curr_end)
            op2 = curr_profit + dp(nxt_indx)

            return max(op1 , op2)
        
        return dp(0)
    
