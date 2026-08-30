class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        
        n = len(nums)
        maxi , mini = max(nums) , min(nums)

        indx1, indx2 = nums.index(maxi) , nums.index(mini)

        # 3 options
        # option1 delte from left
        op1 = max(indx1, indx2) + 1

        # delte from right
        op2 = n - min(indx1 ,indx2)

        # delte from left and right both
        if indx1 < indx2 :
            op3 = indx1+1 + (n-indx2)
        
        else :
            op3 = indx2+1 + (n-indx1)
        
        return min(op1 , op2 , op3)



