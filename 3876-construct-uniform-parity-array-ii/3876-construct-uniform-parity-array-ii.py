# # class Solution:
# #     def uniformArray(self, nums1: list[int]) -> bool:
        
# #         # odd - odd even
# #         # even - even even
# #         # odd - even odd

# #         # temp = sorted(nums1)
# #         odd_candid = []
# #         even_candid = []

# #         n = len(nums1)

# #         for i in range(n):
# #             if nums1[i]%2 == 0 :
# #                 even_candid.append((nums1[i] , i))
            
# #             else :
# #                 odd_candid.append((nums1[i] , i))
        
# #         even_candid.sort()
# #         odd_candid.sort()

# #         # for even
# #         even_chk , odd_chk = True , True


# #         even = []
# #         odd = []
# #         for i in range(n) :
# #             if nums1[i] % 2 == 0 :
# #                 even.append(nums1[i])
# #             else :
# #                 for j in range(len(odd_candid)) :
# #                     val , indx = odd_candid[j]
# #                     if indx == i :
# #                         continue
# #                     else :
# #                         if nums1[i] - val >= 1 :
# #                             even.append(nums1[i] - val)
# #                             break
        

# #         for i in range(n) :
# #             if nums1[i] % 2 == 1 :
# #                 odd.append(nums1[i])
# #             else :

# #                 for j in range(len(odd_candid)) :
# #                     val , indx = odd_candid[j]
# #                     if indx == i :
# #                         continue
# #                     else :
# #                         if nums1[i] - val >= 1 :
# #                             odd.append(nums1[i] - val)
# #                             break

# #         even_chk = len(even) == n
# #         if even_chk : 
# #             for nums in even :
# #                 if nums%2 == 1 :
# #                     even = False
# #                     break
        
# #         odd_chk = len(odd) == n
# #         if odd_chk : 
# #             for nums in odd :
# #                 if nums%2 == 0 :
# #                     odd = False
# #                     break

# #         if even_chk or odd_chk :
# #             return True
        
# #         else :
# #             return False
        


            

# from bisect import bisect_right

# class Solution:
#     def uniformArray(self, nums1: list[int]) -> bool:
#         odd_candid = []
#         even_candid = []

#         n = len(nums1)

#         for i in range(n):
#             if nums1[i] % 2 == 0:
#                 even_candid.append((nums1[i], i))
#             else:
#                 odd_candid.append((nums1[i], i))
        
#         even_candid.sort()
#         odd_candid.sort()

#         even = []
#         odd = []

#         # Constructing target even array using Binary Search
#         for i in range(n):
#             if nums1[i] % 2 == 0:
#                 even.append(nums1[i])
#             else:
#                 # We need val <= nums1[i] - 1.
#                 # bisect_right searches using target threshold
#                 target_val = nums1[i] - 1
                
#                 # Find insertion position for target_val (tuple comparison trick with float('inf'))
#                 idx = bisect_right(odd_candid, (target_val, float('inf'))) - 1

#                 # Walk backwards from the candidate match to find a valid index != i
#                 while idx >= 0:
#                     val, indx = odd_candid[idx]
#                     if indx != i and nums1[i] - val >= 1:
#                         even.append(nums1[i] - val)
#                         break
#                     idx -= 1

#         # Constructing target odd array using Binary Search
#         for i in range(n):
#             if nums1[i] % 2 == 1:
#                 odd.append(nums1[i])
#             else:
#                 target_val = nums1[i] - 1
#                 idx = bisect_right(odd_candid, (target_val, float('inf'))) - 1

#                 while idx >= 0:
#                     val, indx = odd_candid[idx]
#                     if indx != i and nums1[i] - val >= 1:
#                         odd.append(nums1[i] - val)
#                         break
#                     idx -= 1

#         even_chk = len(even) == n
#         odd_chk = len(odd) == n

#         return even_chk or odd_chk

class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        odd_candid = []
        even_candid = []

        n = len(nums1)

        for i in range(n):
            if nums1[i] % 2 == 0:
                even_candid.append((nums1[i], i))
            else:
                odd_candid.append((nums1[i], i))
        
        even_candid.sort()
        odd_candid.sort()

        even = []
        odd = []

        # Constructing target even array in O(1) time per element
        for i in range(n):
            if nums1[i] % 2 == 0:
                even.append(nums1[i])
            else:
                # O(1) direct check: pick smallest valid odd from odd_candid
                if len(odd_candid) > 0:
                    val, indx = odd_candid[0]
                    # If the smallest odd element is at index i, pick the 2nd smallest
                    if indx == i and len(odd_candid) > 1:
                        val, indx = odd_candid[1]
                    
                    if indx != i and nums1[i] - val >= 1:
                        even.append(nums1[i] - val)

        # Constructing target odd array in O(1) time per element
        for i in range(n):
            if nums1[i] % 2 == 1:
                odd.append(nums1[i])
            else:
                # O(1) direct check: pick smallest valid odd from odd_candid
                if len(odd_candid) > 0:
                    val, indx = odd_candid[0]
                    # If the smallest odd element is at index i, pick the 2nd smallest
                    if indx == i and len(odd_candid) > 1:
                        val, indx = odd_candid[1]
                    
                    if indx != i and nums1[i] - val >= 1:
                        odd.append(nums1[i] - val)

        even_chk = len(even) == n
        odd_chk = len(odd) == n

        return even_chk or odd_chk