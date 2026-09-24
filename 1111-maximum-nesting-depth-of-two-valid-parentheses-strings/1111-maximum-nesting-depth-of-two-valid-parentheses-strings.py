class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        
        n = len(seq)
        ans = [0]*(n)
        stack = []

        for i in range(n) :
            curr = seq[i]

            if curr == "(" :
                ans[i] = len(stack)%2
                stack.append(i)
            
            else :
                open_indx = stack.pop()
                ans[i] = ans[open_indx]
        
        return ans