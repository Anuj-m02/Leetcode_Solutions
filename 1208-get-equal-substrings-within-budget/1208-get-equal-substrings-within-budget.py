class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
        n = len(s)
        left , right = 0 , 0 
        total = 0
        ans = float("-inf")

        for right in range(n) :
            diff = abs(ord(s[right]) - ord(t[right]))
            total += diff

            while total > maxCost :
                to_be_remove = abs(ord(s[left]) - ord(t[left]))
                total -= to_be_remove

                left += 1
            
            ans = max(ans , right-left+1)
        
        return ans






