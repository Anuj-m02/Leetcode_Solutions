class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        stack = []
        cnt = 0
        indx = 0
        while indx < n :
            curr = s[indx]
            if curr == "(" :
                stack.append(curr)
                indx += 1
            else :
                if indx+1 < n and s[indx+1] == curr :
                    if stack :
                        stack.pop()
                    else :
                        cnt += 1
                    indx += 2
                else :
                    if stack :
                        stack.pop()
                        cnt += 1
                    else :
                        cnt += 2
                    indx += 1
        cnt += 2*len(stack)
        return cnt
