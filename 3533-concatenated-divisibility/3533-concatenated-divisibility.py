from collections import defaultdict , deque , Counter
import heapq
from functools import lru_cache


class Solution:
    def concatenatedDivisibility(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)
        nums.sort()
        # 10^length % k and x%k
        mult = [pow(10 , len(str(x)), k) for x in nums]
        nums_mod = [x % k for x in nums]


        @lru_cache(maxsize=None)
        def dp(used_set , rem) :

            if len(used_set) == n :
                return [] if rem == 0  else None
            
            for i in range(n) :
                if i not in used_set :
                    nxt_rem = (rem * mult[i] + nums_mod[i]) % k
                    sub_res = dp(used_set | frozenset({i}) , nxt_rem)

                    if sub_res is not None :
                        return [nums[i]] + sub_res

            return None
        
        ans = dp(frozenset() , 0)
        return ans if ans is not None else []




