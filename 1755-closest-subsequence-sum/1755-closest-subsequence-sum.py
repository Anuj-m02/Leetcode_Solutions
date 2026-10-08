# class Solution:
#     def minAbsDifference(self, nums: list[int], goal: int) -> int:


#         n = len(nums)
#         left_nums = nums[:n//2]
#         right_nums = nums[n//2 :]

#         @cache
#         def dp_left(indx , curr_sum) :
#             if indx == len(left_nums) :
#                 return {curr_sum}
            
#             return dp_left(indx+1 , curr_sum) | dp_left(indx+1 , curr_sum + left_nums[indx])

#         @cache
#         def dp_right(indx , curr_sum) :
#             if indx == len(right_nums) :
#                 return {curr_sum}
            
#             return dp_right(indx+1 , curr_sum) | dp_right(indx+1 , curr_sum + right_nums[indx])
        

#         left_sums = list(dp_left(0,0))
#         right_sums = sorted(dp_right(0,0))

#         ans = float("inf")
#         m = len(right_sums)

#         for s in left_sums :
#             target = goal - s
#             indx = bisect.bisect_left(right_sums , target)

#             if indx < m :
#                 ans = min(ans , abs(goal - (s+right_sums[indx])))
            
#             if indx > 0 :
#                 ans = min(ans , abs(goal - (s + right_sums[indx-1])))
            
#             if ans == 0 :
#                 return 0
        
#         return ans

import bisect

class Solution:
    def minAbsDifference(self, nums: list[int], goal: int) -> int:
        n = len(nums)
        left_nums = nums[:n // 2]
        right_nums = nums[n // 2:]

        # Helper function using explicit memoization (set/dict) 
        # and populating a shared array instead of returning sets.
        def get_subset_sums(arr):
            memo = set()
            res = []
            
            def dp(idx, curr_sum):
                state = (idx, curr_sum)
                if state in memo:
                    return
                memo.add(state)
                
                if idx == len(arr):
                    res.append(curr_sum)
                    return
                
                # Take
                dp(idx + 1, curr_sum + arr[idx])
                # Don't take
                dp(idx + 1, curr_sum)
                
            dp(0, 0)
            return res

        left_sums = get_subset_sums(left_nums)
        right_sums = sorted(get_subset_sums(right_nums))

        ans = float("inf")
        m = len(right_sums)

        for s in left_sums:
            target = goal - s
            indx = bisect.bisect_left(right_sums, target)

            if indx < m:
                ans = min(ans, abs(goal - (s + right_sums[indx])))
            
            if indx > 0:
                ans = min(ans, abs(goal - (s + right_sums[indx - 1])))
            
            if ans == 0:
                return 0
        
        return ans

        # n = len(nums)
        # nums.sort()

        # pos_sum = [0]*(n+1)
        # neg_sum = [0]*(n+1)

        # for i in range(n-1 , -1 , -1):
        #     pos_sum[i] = pos_sum[i+1] + max(0 , nums[i])
        #     neg_sum[i] = neg_sum[i+1] + min(0 , nums[i])
        
        # ans = float("inf")

        # @lru_cache(maxsize=None)
        # def dp(indx , curr_sum) :
        #     nonlocal ans

        #     diff = abs(curr_sum - goal)
        #     ans = min(ans , diff)

        #     if diff == 0 or indx >= n :
        #         return diff
            
        #     if curr_sum + pos_sum[indx] < goal - ans :
        #         return abs(goal - (curr_sum + pos_sum[indx]))
            

        #     if curr_sum + neg_sum[indx] > goal + ans :
        #         return abs(goal - (curr_sum + neg_sum[indx]))

        #     take = dp(indx+1 , curr_sum + nums[indx])
        #     not_take = dp(indx+1 , curr_sum)

        #     return min(take , not_take)
        
        # return dp(0 , 0)
        
        # n = len(nums)
        # nums.sort()

        # total = sum(nums)
        # if total <= goal :
        #     return goal - total
        
        # mini = float("inf")
        
        # @lru_cache(maxsize=None)
        # def dp(indx , curr_sum) :
            
        #     if indx >= n :
        #         return abs(goal - curr_sum)
            

        #     not_take = dp(indx+1 , curr_sum)

        #     take = dp(indx+1 , curr_sum + nums[indx])

        #     return min(take , not_take)
        
        # return dp(0 , 0)
