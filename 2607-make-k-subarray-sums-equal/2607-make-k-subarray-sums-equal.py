class Solution:
    def makeSubKSumEqual(self, arr: list[int], k: int) -> int:
        
        n = len(arr)
        g = math.gcd(n , k)
        ans = 0

        for start in range(g) :
            grp = sorted(arr[indx] for indx in range(start , n , g))
            median = grp[len(grp)//2]
            ans += sum(abs(val - median) for val in grp)
        
        return ans


