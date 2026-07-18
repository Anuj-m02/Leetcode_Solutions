class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        n = len(s)

        diff = [0]*(n+1)
        # for forward take +1 , for backward take -1 , then take prefix sum

        for indx , val in enumerate(shifts) :

            start , end , direction = val

            if direction == 1 :
                diff[start] += 1
                diff[end+1] -= 1
            
            if direction == 0 :
                diff[start] -= 1
                diff[end+1] += 1
            
        print(diff)
        for i in range(1,n):
            diff[i] += diff[i-1]
        print(diff)
        ans = []

        for i in range(n) :
            x = ord(s[i]) - ord("a")
            x = (x+diff[i])%26
            ans.append(chr(x+ord("a")))
        
        return "".join(ans)
