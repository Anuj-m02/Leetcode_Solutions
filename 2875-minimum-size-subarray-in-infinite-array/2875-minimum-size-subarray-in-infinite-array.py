class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        
        total_sum = sum(nums)
        n = len(nums)

        full_cycles = target // total_sum
        rem_target = target % total_sum

        if rem_target == 0 :
            return full_cycles*n
        
        prefix_map = {0 : -1}
        curr_sum = 0 
        min_len = float("inf")

        double_nums = nums + nums

        for i , val in enumerate(double_nums) :
            curr_sum += val

            if (curr_sum - rem_target) in prefix_map :
                min_len = min(min_len , i - prefix_map[curr_sum - rem_target])
            
            prefix_map[curr_sum] = i
        
        if min_len == float("inf") :
            return -1
        
        return full_cycles*n + min_len