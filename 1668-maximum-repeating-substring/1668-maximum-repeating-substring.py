class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        

        n , m = len(sequence) , len(word)
        max_k = n//m
        ans = 0
        for i in range(max_k+1) :
            curr_str = word*i
            if curr_str in sequence :
                ans = max(ans , i)
        
        return ans
