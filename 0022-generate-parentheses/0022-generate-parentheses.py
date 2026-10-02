class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def help(n,open,close,path) :
            if open == close == n :
                ans.append(path)
                return ans
            if open < n :
                help(n,open+1,close,path+"(")
            if open > close :
                help(n,open,close+1,path+")")
        help(n,0,0,"")
        return ans
