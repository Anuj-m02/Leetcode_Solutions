class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi = -1
        check = False
        curr = 0
        for i in range(len(nums)):
            if nums[i] == 1 and check == False :
                curr = 1
                maxi = max(maxi,curr)
                check = True
            if nums[i] == 1 and check == True :
                curr += 1
                maxi = max(maxi,curr)
            if nums[i] != 1 :
                check = False
        if maxi < 0 :
            return 0
        else :
            return maxi-1