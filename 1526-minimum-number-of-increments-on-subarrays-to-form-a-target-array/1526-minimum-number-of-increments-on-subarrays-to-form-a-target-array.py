class Solution:
    def minNumberOperations(self, target: list[int]) -> int:
        
        n = len(target)
        res , prev = 0, 0
        for x in target :
            if x > prev :
                res += x-prev
            
            prev = x
        
        return res

        #