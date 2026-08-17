# from collections import defaultdict , deque , Counter
# import heapq
# from functools import lru_cache

# class Solution:
#     def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        
#         n = len(aliceValues)

#         alice = []
#         for i , val in aliceValues :
#             alice.append((val,i))
#         alice.sort(reverse=True)
#         bob = []
#         for i , val in bobValues :
#             bob.append((val , i))
#         bob.sort(reverse=True)
        
#         indx_used = set()
#         a , b = 0 , 0
        
#         indx1 , indx2 = 0 , 0
#         i = 0
#         while i < n :

#             # alice turn
#             if i%2 == 0 :
#                 if indx1 not in indx_used :
#                     a += alice[indx1][0]
#                     indx_used.add(alice[indx1][1])
                
#                 else :
#                     indx1 = get_nxt_indx(indx1 , indx_used)
#                     a += alice[indx1][0]
#                     indx_used.add(alice[indx1][1])
            
#             else :
#                 if indx2 not in indx_used :
#                     b += bob[indx2][0]
#                     indx_used.add(bob[indx2][1])
                
#                 else :
#                     indx2 = get_nxt_indx(indx2 , indx_used)
#                     b += bob[indx2][0]
#                     indx_used.add(bob[indx2][1])
            
#             i += 1
        

#         if a == b :
#             return 0
        
#         if a > b :
#             return 1
        
#         if b > a :
#             return -1




from typing import List

class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        # Combine values by sum of priorities along with individual scores
        stones = []
        for i in range(len(aliceValues)):
            total_val = aliceValues[i] + bobValues[i]
            stones.append((total_val, aliceValues[i], bobValues[i]))
        
        # Sort stones by total value in descending order
        stones.sort(reverse=True)
        
        alice_score = 0
        bob_score = 0
        
        # Take turns picking the best remaining stone
        for i, (total, a_val, b_val) in enumerate(stones):
            if i % 2 == 0:
                alice_score += a_val
            else:
                bob_score += b_val
                
        if alice_score > bob_score:
            return 1
        elif bob_score > alice_score:
            return -1
        else:
            return 0