class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        
        n = len(nums)
        nums.sort()
        indx1 = bisect.bisect_left(nums , target)
        indx2 = bisect.bisect_right(nums , target)

        res = []
        for i in range(indx1, indx2) :
            res.append(i)
        
        return res

