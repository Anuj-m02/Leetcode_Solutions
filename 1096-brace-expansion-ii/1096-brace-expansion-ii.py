class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        
        n = len(expression)
        grps = []
        stack = []
        curr = [""]

        for char in expression :
            if char.isalpha() :

                curr = [s + char for s in curr]
            
            elif char == "{" :
                stack.append((grps , curr))
                grps, curr = [] , [""]
            
            elif char == "," :
                grps.append(curr)
                curr = [""]
            
            elif char == "}" :
                grps.append(curr)
                
                union_set = set()

                for g in grps :
                    union_set.update(g)
                
                prev_grps , prev_curr = stack.pop()
                curr = [p + u for p in prev_curr for u in union_set]
                grps = prev_grps
            
        grps.append(curr)
        res = set()
        for g in grps :
            res.update(g)
        
        return sorted(list(res))

