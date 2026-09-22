# class Solution:
#     def compareVersion(self, version1: str, version2: str) -> int:
        
#         n , m = len(version1) , len(version2)
#         i , j = 0 , 0

#         while i < n or j < m :
#             num1 = 0

#             while i < n and version1[i] != "." :
#                 num1 = num1*10 + int(version1[i])
#                 i += 1
            
#             num2 = 0 
#             while j < m and version2[j] != "." :
#                 num2 = num2*10 + int(version2[j])
#                 j += 1
            
#             if num1 < num2 :
#                 return -1
#             if num1 > num2 :
#                 return 1
            
#             i += 1
#             j += 1
        
#         return 0
class Solution(object):
    def compareVersion(self, version1, version2):
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))

        while len(v1) < len(v2):
            v1.append(0)
        while len(v2) < len(v1):
            v2.append(0)

        for a, b in zip(v1, v2):
            if a < b:
                return -1
            elif a > b:
                return 1

        return 0