class Solution:
    def minOperations(self, k: int) -> int:
        
        if k == 1 :
            return 0

        cnt = float("inf")
        for ele in range(1,k+1) :
            inc = ele-1
            dup = math.ceil(k/ele) - 1

            cnt = min(cnt , inc + dup)
        
        return cnt

