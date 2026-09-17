class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        
        n = len(arr)

        subarrays = []
        prefix_map = {0 : -1}
        curr_sum = 0

        for i , val in enumerate(arr) :
            curr_sum += val
            needed = curr_sum-target
            if needed in prefix_map :
                subarrays.append((prefix_map[needed] + 1 , i))
            
            prefix_map[curr_sum] = i
        
        # print(prefix_map)
        # print(subarrays)
        
        m = len(subarrays)
        if m < 2 :
            return -1
        
        starts = [s[0] for s in subarrays]

        @lru_cache(maxsize=None)
        def dp(indx , cnt) :
            if cnt == 0 :
                return 0
            if indx >= m :
                return float("inf")

            #skip this subarrys
            res = dp(indx+1 , cnt) 

            start , end = subarrays[indx]
            curr_len = end-start+1
            
            nxt_indx = bisect.bisect_right(starts , end)
            res = min(res , curr_len + dp(nxt_indx , cnt-1))

            return res
        
        ans = dp(0,2)
        return ans if ans != float("inf") else -1
