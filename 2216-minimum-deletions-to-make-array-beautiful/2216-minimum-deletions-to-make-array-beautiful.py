class Solution:
    def minDeletion(self, nums: list[int]) -> int:
        
        n = len(nums)
        stack = []
        cnt = 0

        for num in nums :

            if len(stack) % 2 == 1 and stack[-1] == num :
                continue # skip this ele

            stack.append(num)


        if len(stack)%2 == 1 :
            stack.pop()

        return len(nums) - len(stack) 