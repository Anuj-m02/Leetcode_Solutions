class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        res = set()
        used = [False]*(len(digits))

        def recur(path):
            if len(path) == 3 :
                num = int("".join(map(str,path)))
                if num%2 == 0 and path[0] != 0 :
                    res.add(num)
                return 
            
            for i in range(len(digits)):
                if not used[i] :
                    used[i] = True
                    path.append(digits[i])
                    recur(path)
                    path.pop()
                    used[i] = False
        recur([])
        return len(res)