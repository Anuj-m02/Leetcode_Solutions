class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num)
        
        # Check if '6' exists to avoid a ValueError
        if "6" in s:
            indx1 = s.index("6")
            
            # Convert string directly to a list of characters: ['9', '6', '6', '9']
            arr = list(s)
            
            # Modify the character at the found index
            arr[indx1] = "9"
            
            # Rejoin the array into a string
            res = "".join(arr)
            return int(res)
            
        return num