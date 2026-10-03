class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        

        n = len(s)

        unique = set(s)
        if len(unique) <= k :
            return 0
        
        cnts = [s.count(char) for char in unique]

        cnts.sort()

        num_to_remove = len(unique) - k

        return sum(cnts[:num_to_remove])