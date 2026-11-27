class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def next(arr):
            res = [1]
            for i in range(1,len(arr)):
                curr = arr[i]+arr[i-1]
                res.append(curr)
            res.append(1)
            return res
        ans = [[1],[1,1]]
        arr = [1,1]
        if numRows == 1 :
            return [[1]]
        if numRows == 2 :
            return [[1],[1,1]]
        while numRows > 2 :
            currarr = next(arr)
            ans.append(currarr)
            arr = currarr
            numRows -= 1
        return ans
