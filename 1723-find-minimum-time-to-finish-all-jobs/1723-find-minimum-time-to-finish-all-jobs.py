# class Solution:
#     def minimumTimeRequired(self, jobs: list[int], k: int) -> int:
        
#         n = len(jobs)

#         jobs.sort(reverse=True)

#         @lru_cache
#         def dp(remaining , curr_load , k_left) :

#             if not remaining :
#                 return curr_load
            
#             if k_left == 1 :
#                 return curr_load + sum(jobs[i] for i in remaining)
            

#             # new worker
#             ans = max(curr_load , dp(remaining , 0 , k_left-1 ))

#             if curr_load >= ans :
#                 return ans

#             # add job to curr workere
#             rem_list = list(remaining)
#             for i in rem_list :
#                 nxt_rem = remaining - {i}
#                 res = dp(nxt_rem , curr_load + jobs[i] , k_left)
#                 ans = min(ans , res)

#                 if curr_load == 0 :
#                     break
            

#             return ans
        

#         initial_jobs = frozenset(range(n))
#         return dp(initial_jobs , 0 , k)



from functools import lru_cache
from itertools import combinations

class Solution:
    def minimumTimeRequired(self, jobs: list[int], k: int) -> int:
        n = len(jobs)
        
        # Precompute sum of any frozenset of job indices to avoid repeated work
        @lru_cache(maxsize=None)
        def get_subset_sum(subset: frozenset) -> int:
            return sum(jobs[i] for i in subset)

        @lru_cache(maxsize=None)
        def dp(remaining: frozenset, k_left: int) -> int:
            # Base Case 1: All jobs assigned
            if not remaining:
                return 0
            
            # Base Case 2: 1 worker left -> must take all remaining jobs
            if k_left == 1:
                return get_subset_sum(remaining)

            # Symmetry Breaking: Force the first element into the current worker's subset
            first_elem = next(iter(remaining))
            other_elems = list(remaining - {first_elem})
            
            ans = float('inf')

            # Generate all combinations of other_elems without any bitmasking
            for r in range(len(other_elems) + 1):
                for combo in combinations(other_elems, r):
                    # Form the subset for the current worker
                    curr_worker_set = frozenset((first_elem,) + combo)
                    curr_cost = get_subset_sum(curr_worker_set)

                    # Early pruning: if single worker cost already exceeds ans, skip
                    if curr_cost >= ans:
                        continue

                    rest_set = remaining - curr_worker_set
                    rest_cost = dp(rest_set, k_left - 1)

                    ans = min(ans, max(curr_cost, rest_cost))

            return ans

        initial_jobs = frozenset(range(n))
        return dp(initial_jobs, k)