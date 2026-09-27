from collections import defaultdict , deque , Counter

class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        
        ans = []
        nums.sort()
        d = Counter(nums)

        while d :
            keys = list(d.keys())
            ans.extend(keys)

            for key in keys :
                d[key] -= 1
                if d[key] == 0 :
                    del d[key]
        
        return ans 

  