class Solution:
    def minLights(self, lights: list[int]) -> int:
        
        n = len(lights)
        cnt = 0

        vis = [0]*(n+1)

        for indx , val in enumerate(lights) :
            if val :
                left = max(0 , indx-val)
                right = min(n-1 , indx+val)
            
                vis[left] += 1
                vis[right+1] -= 1
        
        ans = 0
        curr = 0
        gap = 0

        for i in range(n):
            curr += vis[i]
            if curr == 0 :
                gap += 1
            else :
                if gap :
                    ans += (gap+2)//3
                    gap = 0
        
        if gap :
            ans += (gap+2)//3
        

        return ans