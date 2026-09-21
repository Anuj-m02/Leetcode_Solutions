class Solution:
    def minInversionCount(self, nums: List[int], k: int) -> int:
        
        n = len(nums)

        # def f(arr) :
        #     n = len(arr)
        #     cnt = 0
        #     for i in range(n) :
        #         for j in range(i+1 , n) :
        #             if arr[i] > arr[j] :
        #                 cnt += 1
        #     return cnt

        # left , right = 0 , 0 
        # cnt = float("inf")
        # for right in range(n) :

        #     if right-left+1 > k :
        #         left += 1
            
        #     if right-left+1 == k :
        #         cnt = min(cnt , f(nums[left:right+1]))
        
        # return cnt

        sl = SortedList()
        curr_inversion = 0

        for i in range(k) :
            val = nums[i]
            greater_cnt = len(sl) - sl.bisect_right(val)
            curr_inversion += greater_cnt
            sl.add(val)
        
        min_inversion = curr_inversion


        for i in range(k , n) :
            # remove left val
            left_val = nums[i-k]
            smaller_cnt = sl.bisect_left(left_val)
            curr_inversion -= smaller_cnt
            sl.remove(left_val)

            # add right val
            right_val = nums[i]
            greater_cnt = len(sl) - sl.bisect_right(right_val)
            curr_inversion += greater_cnt
            sl.add(right_val)

            min_inversion = min(min_inversion , curr_inversion)
        
        return min_inversion
