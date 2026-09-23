# class Solution:
#     def minOperations(self, nums: list[int]) -> int:
        
#         # compute all palindromes upto 1e5 if changed to string then length 5 only easy to compute maybe 
#         # segregate in odd and even
#         #[1,2,3,4,5,6,7,8,9,11,22,33,44,55,66,77,88,99,101,111,121,131,141,151...]


#         odd_pal = []
#         even_pal = []

#         if not odd_pal :
            
#             # single digits
#             for i in range(1 , 10) :
#                 (even_pal if i%2 == 0 else odd_pal).append(i)
            
#             # prefix mirroring upto 1e5
#             for root in range(1 , int(1e5)) :
#                 s = str(root)
#                 rev = s[::-1]

#                 # evenlength 12 - 1221
#                 p1 = int(s + rev)
#                 (even_pal if p1%2 == 0 else odd_pal).append(p1)

#                 # odd length 12 mid 3 12321
#                 for mid in range(10) :
#                     p2 = int(s + str(mid) + rev)
#                     (even_pal if p2%2 == 0 else odd_pal).append(p2)
        
#         odd_pal.sort()
#         even_pal.sort()
 


#         # for num in range(1 , 100000) :
#         #     s = str(num)
#         #     if num%2 :
#         #         if s == s[::-1] :
#         #             odd_pal.append(num)

#         #     else :
#         #         if s == s[::-1] :
#         #             even_pal.append(num)
                

#         n = len(nums)
#         cnt = 0
#         for num in nums :
#             if num%2 :
#                 # check odd
#                 indx1 = bisect.bisect_left(odd_pal ,  num)
#                 # indx1 gives >= num , indx1-1 gives < num
#                 candidates = []
#                 if indx1 < len(odd_pal) :
#                     # go to nxt bigger or equal
#                     candidates.append(odd_pal[indx1])
#                 if indx1 > 0 :
#                     # go to smaller
#                      candidates.append(odd_pal[indx1-1])                   

#                 steps = min(abs(num-p)//2 for p in candidates)
            
#             else:
#                 # check even
#                 indx1 = bisect.bisect_left(even_pal, num)
                
#                 # indx1 gives >= num, indx1 - 1 gives < num
#                 candidates = []
#                 if indx1 < len(even_pal):
#                     candidates.append(even_pal[indx1])
#                 if indx1 > 0:
#                     candidates.append(even_pal[indx1 - 1])

#                 steps = min(abs(num - p) // 2 for p in candidates)
            
#             cnt += steps
        
#         return cnt


import bisect

# Precompute palindromes up to ~2 * 10^9 outside the class
odd_pal = []
even_pal = []

if not odd_pal:
    # 1. Single digits
    for i in range(1, 10):
        (even_pal if i % 2 == 0 else odd_pal).append(i)
        
    # 2. Prefix mirroring up to 100,000 (creates 5 to 10-digit palindromes)
    for root in range(1, 100000):
        s = str(root)
        rev = s[::-1]
        
        # Even length (e.g. 12 -> 1221)
        p1 = int(s + rev)
        (even_pal if p1 % 2 == 0 else odd_pal).append(p1)
        
        # Odd length (e.g. 12, mid=3 -> 12321)
        for mid in range(10):
            p2 = int(s + str(mid) + rev)
            (even_pal if p2 % 2 == 0 else odd_pal).append(p2)

    odd_pal.sort()
    even_pal.sort()


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        cnt = 0
        for num in nums:
            if num % 2:
                # check odd
                indx1 = bisect.bisect_left(odd_pal, num)
                candidates = []
                if indx1 < len(odd_pal):
                    candidates.append(odd_pal[indx1])
                if indx1 > 0:
                    candidates.append(odd_pal[indx1 - 1])

                steps = min(abs(num - p) // 2 for p in candidates)
            
            else:
                # check even
                indx1 = bisect.bisect_left(even_pal, num)
                candidates = []
                if indx1 < len(even_pal):
                    candidates.append(even_pal[indx1])
                if indx1 > 0:
                    candidates.append(even_pal[indx1 - 1])

                steps = min(abs(num - p) // 2 for p in candidates)
            
            cnt += steps
        
        return cnt