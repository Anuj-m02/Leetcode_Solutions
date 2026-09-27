# class Solution:
#     def maxEqualAdjacentPairs(self, nums: list[int]) -> int:
        
#         n = len(nums)



    
#         # # highest_cnt
#         # d = Counter(nums)

#         # if len(d) == 1 :
#         #     return d[nums[0]] - 1

#         # max_cnt , max_val = 0 , 0
#         # second_max_cnt , second_max_val = 0 , 0

#         # sorted_items = sorted(d.items(), key=lambda x: x[1], reverse=True)

#         # return (sorted_items[0][1] + sorted_items[1][1] - 1)

from collections import Counter, defaultdict

class Solution:
    def maxEqualAdjacentPairs(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
            
        base_pairs = 0
        pair_counts = defaultdict(Counter)

        for i in range(n - 1):
            u, v = nums[i], nums[i + 1]
            if u == v:
                base_pairs += 1
            else:
                pair_counts[u][v] += 1
                pair_counts[v][u] += 1

        max_extra = 0
        for u in pair_counts:
            for v in pair_counts[u]:
                max_extra = max(max_extra, pair_counts[u][v])

        return base_pairs + max_extra