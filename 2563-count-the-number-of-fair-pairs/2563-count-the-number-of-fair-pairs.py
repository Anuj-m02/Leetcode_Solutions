class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:

        n = len(nums)

        # prefix = [0]*(n)
        # for i in range(n) :
        #     prefix[i] = prefix[i-1] + nums[i]


        nums.sort()

        left , right = 0 , n-1
        cnt = 0

        for i in range(n) :

            min_val = lower - nums[i]
            max_val = upper - nums[i]

            left_indx = bisect.bisect_left(nums , min_val , i+1 , n)
            right_indx = bisect.bisect_right(nums , max_val , i+1 , n)

            cnt += (right_indx - left_indx)
        
        return cnt

        # while left <= right :
        #     curr = nums[left] + nums[right]

        #     if lower <= curr <= upper :
        #         cnt += (nc2)
            
        #     if curr > upper :
        #         right -= 1
        #     elif curr < lower :
        #         left += 1
        
        # return cnt