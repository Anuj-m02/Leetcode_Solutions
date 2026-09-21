# # # class Solution:
# # #     def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        
# # #         n = len(nums)

# # #         ans = [0]*(n-k+1)

# # #         heap = []
# # #         d = defaultdict(int)
# # #         # -cnt , -val so that top x frequent
# # #         for indx in range(k) :
# # #             d[nums[indx]] += 1
        
# # #         for val,cnt in d.items() :
# # #             heapq.heappush(heap , (-cnt , -val))
        
# # #         count = 0
# # #         while cnt <= x :
# # #             -cnt , -val =  heapq.heappop(heap)
# # #             ans[0] += (cnt*val)
        
# # #         left = 0
# # #         right = k+1
# # #         while right < n :
# # #             curr_cnt , curr_val = d[nums[left]] , nums[left]
# # #             d[nums[left]] -= 1
# # #             # lazy_deletion_mthd logn
# # #             heapq.heappop(heap , (-curr_cnt , curr_val))

# # #             left += 1




# # from collections import defaultdict
# # import heapq
# # from typing import List

# # class Solution:
# #     def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
# #         n = len(nums)
# #         ans = [0] * (n - k + 1)
# #         d = defaultdict(int)

# #         # Build initial frequency map for first window
# #         for indx in range(k):
# #             d[nums[indx]] += 1

# #         # Helper to compute x-sum for current frequency map
# #         def get_x_sum():
# #             heap = []
# #             for val, cnt in d.items():
# #                 if cnt > 0:
# #                     # Push (-cnt, -val) to pop most frequent / larger value first
# #                     heapq.heappush(heap, (-cnt, -val))
            
# #             total_sum = 0
# #             items_taken = 0
# #             while heap and items_taken < x:
# #                 neg_cnt, neg_val = heapq.heappop(heap)
# #                 total_sum += (-neg_cnt) * (-neg_val)
# #                 items_taken += 1
# #             return total_sum

# #         ans[0] = get_x_sum()

# #         # Slide window across array
# #         left = 0
# #         for right in range(k, n):
# #             # Slide window: remove outgoing, add incoming
# #             d[nums[left]] -= 1
# #             d[nums[right]] += 1
# #             left += 1

# #             ans[left] = get_x_sum()

# #         return ans

# from collections import defaultdict
# import heapq
# from typing import List


# class Solution:
#     def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:

#         n = len(nums)
#         ans = [0] * (n - k + 1)

#         d = defaultdict(int)
#         version = defaultdict(int)

#         # Build initial frequency map
#         for i in range(k):
#             d[nums[i]] += 1

#         # Heap:
#         # (-frequency, -value, version)
#         heap = []

#         for val, cnt in d.items():
#             version[val] += 1
#             heapq.heappush(
#                 heap,
#                 (-cnt, -val, version[val])
#             )

#         def get_x_sum():

#             total_sum = 0
#             items_taken = 0
#             stashed = []

#             while heap and items_taken < x:

#                 neg_cnt, neg_val, ver = heapq.heappop(heap)

#                 cnt = -neg_cnt
#                 val = -neg_val

#                 # Check whether this is the latest version
#                 if version[val] != ver:
#                     continue

#                 # Check whether frequency is still correct
#                 if d[val] != cnt:
#                     continue

#                 total_sum += cnt * val
#                 items_taken += 1

#                 stashed.append(
#                     (neg_cnt, neg_val, ver)
#                 )

#             # Put valid entries back
#             for item in stashed:
#                 heapq.heappush(heap, item)

#             return total_sum

#         ans[0] = get_x_sum()

#         left = 0

#         for right in range(k, n):

#             out_val = nums[left]
#             in_val = nums[right]

#             # -----------------------
#             # Remove outgoing element
#             # -----------------------

#             d[out_val] -= 1
#             version[out_val] += 1

#             if d[out_val] > 0:
#                 heapq.heappush(
#                     heap,
#                     (
#                         -d[out_val],
#                         -out_val,
#                         version[out_val]
#                     )
#                 )

#             # -----------------------
#             # Add incoming element
#             # -----------------------

#             d[in_val] += 1
#             version[in_val] += 1

#             heapq.heappush(
#                 heap,
#                 (
#                     -d[in_val],
#                     -in_val,
#                     version[in_val]
#                 )
#             )

#             left += 1

#             ans[left] = get_x_sum()

#         return ans

from collections import Counter
from sortedcontainers import SortedList
from typing import List

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        ans = []
        counts = Counter()
        
        top = SortedList()  # Stores top x (count, val)
        bot = SortedList()  # Stores remaining (count, val)
        top_sum = 0
        
        def add(val):
            nonlocal top_sum
            cnt = counts[val]
            if cnt == 0: return
            item = (cnt, val)
            if top and item > top[0]:
                top.add(item)
                top_sum += cnt * val
            else:
                bot.add(item)
                
        def remove(val):
            nonlocal top_sum
            cnt = counts[val]
            if cnt == 0: return
            item = (cnt, val)
            if item in top:
                top.remove(item)
                top_sum -= cnt * val
            else:
                bot.remove(item)
                
        def balance():
            nonlocal top_sum
            while len(top) > x:
                smallest = top.pop(0)
                top_sum -= smallest[0] * smallest[1]
                bot.add(smallest)
            while len(top) < x and bot:
                largest = bot.pop(-1)
                top.add(largest)
                top_sum += largest[0] * largest[1]

        # Process first window
        for i in range(k):
            counts[nums[i]] += 1
        for val in counts:
            add(val)
        balance()
        ans.append(top_sum)
        
        # Slide window
        for right in range(k, n):
            out_val, in_val = nums[right - k], nums[right]
            if out_val != in_val:
                remove(out_val)
                counts[out_val] -= 1
                add(out_val)
                
                remove(in_val)
                counts[in_val] += 1
                add(in_val)
                
                balance()
            ans.append(top_sum)
            
        return ans
