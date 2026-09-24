class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        
        n = len(locked)

        if n%2 :
            return False
        
        open_stack = [] # indices of locked "("
        unlocked_stack = [] # indices of unlocked pos "0"


        for i in range(n) :
            if locked[i] == "0" :
                unlocked_stack.append(i)
            
            elif s[i] == "(" :
                open_stack.append(i)
            
            elif s[i] == ")" :
                if open_stack :
                    open_stack.pop()
                elif unlocked_stack :
                    unlocked_stack.pop()
                else :
                    return False

        while open_stack and unlocked_stack :
            if open_stack[-1] < unlocked_stack[-1] :
                open_stack.pop()
                unlocked_stack.pop()
            else :
                return False
        
        return len(open_stack) == 0