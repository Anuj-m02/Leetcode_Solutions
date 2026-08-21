class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        n , m = len(mat) , len(mat[0])

        final = []
        for row in range(n) :
            count_1 = mat[row].count(1)
            final.append((count_1 , row))
        
        final.sort()

        ans = []
        for i in range(k) :
            ans.append(final[i][1])
        
        return ans
