class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        cnt = Counter(int(ch) for ch in num)
        total = sum(int(ch) for ch in num)

        @cache
        def dfs(i, odd, even, balance):
            if odd == 0 and even == 0 and balance == 0:
                return 1
            if i < 0 or odd < 0 or even < 0 or balance < 0:
                return 0
            res = 0
            for j in range(0, cnt[i] + 1):
                res += comb(odd, j) * comb(even, cnt[i] - j) * dfs(i - 1, odd - j, even - cnt[i] + j, balance - i * j)
            return res % 1000000007

        return 0 if total % 2 else dfs(9, len(num) - len(num) // 2, len(num) // 2, total // 2)


# class Solution:
#     def countBalancedPermutations(self, num: str) -> int:
        

#         n = len(num)
#         mod = int(1e7)

#         counts = Counter(num)
#         total_sum = sum(int(c) for c in num)

#         if total_sum % 2 != 0 :
#             return 0
        
#         target_sum = total_sum // 2
#         max_even_cnt = (n+1)//2
#         max_odd_cnt = (n//2)

#         digits = list(counts.keys())
#         num_digits = len(digits)

#         @lru_cache(maxsize=None)
#         def dp(indx , even_cnt , curr_even_sum) :

#             if indx >= num_digits :
#                 if even_cnt == max_even_cnt and curr_even_sum == target_sum :
#                     return 1
#                 else :
#                     return 0
            
#             d = digits[indx]
#             cnt = counts[d]
#             ans = 0

#             # count odd pos filled 
#             odd_cnt = sum(counts[digits][k] for k in range(indx)) - even_cnt
#             rem_even_slots = max_even_cnt - even_cnt
#             rem_odd_slots = max_odd_cnt - odd_cnt


