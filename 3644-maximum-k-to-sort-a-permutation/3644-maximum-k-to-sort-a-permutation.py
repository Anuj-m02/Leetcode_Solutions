class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        
        ans = None

        for indx , val in enumerate(nums) :
            if val != indx :
                if ans is None :
                    ans = val
                else :
                    ans = ans & val
        
        return ans if ans is not None else 0