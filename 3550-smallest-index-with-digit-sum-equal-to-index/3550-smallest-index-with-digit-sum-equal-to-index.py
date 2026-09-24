class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        
        n = len(nums)

        for i in range(n) :
            curr_str = str(nums[i])
            cnt = 0
            for string in curr_str :
                cnt += int(string)
            
            if cnt == i :
                return i
        
        return -1