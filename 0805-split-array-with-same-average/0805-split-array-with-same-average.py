class Solution:
    def splitArraySameAverage(self, nums: list[int]) -> bool:
        n = len(nums)
        total = sum(nums)

        # target sum is 0 now
        arr = [x*n - total for x in nums]
        left = arr[:n//2]
        right = arr[n//2:]

        def subset_map(arr) :
            m = len(arr)
            sums_by_cnt = {i : set() for i in range(m+1)}

            @lru_cache(maxsize=None)
            def dp(indx , curr_sum , cnt) :
                if indx == m :
                    sums_by_cnt[cnt].add(curr_sum)
                    return
                
                dp(indx+1 , curr_sum , cnt)
                dp(indx+1 , curr_sum + arr[indx] , cnt+1)
            
            dp(0,0,0)
            return sums_by_cnt
        
        left_sums = subset_map(tuple(left))
        right_sums = subset_map(tuple(right))

        for k_left , s_left_set in left_sums.items():
            for k_right , s_right_set in right_sums.items() :

                if k_left+k_right == 0 or k_left+k_right == n :
                    continue
                
                for s_left in s_left_set :
                    if -s_left in s_right_set :
                        return True
        
        return False





        # @lru_cache(maxsize=None)
        # def dp(indx , total_left , cnt_left):

        #     if cnt_left >= n :
        #         return False

        #     if indx >= n :
        #         if 0 < cnt_left < n :
        #             avg_left = total_left/cnt_left
        #             cnt_right = n - cnt_left
        #             avg_right = (total-total_left) / cnt_right
        #             if avg_left == avg_right :
        #                 return True
        #         return False
                
            
        #     # not pick this indx in total_left
        #     not_take = dp(indx+1 , total_left , cnt_left)
        #     take = dp(indx+1 , total_left + nums[indx] , cnt_left + 1)
        #     return take or not_take
        
        # return dp(0 , 0 , 0)