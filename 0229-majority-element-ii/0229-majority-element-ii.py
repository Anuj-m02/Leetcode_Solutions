import math

#YAHA PR BOORE MOORE VOTING ALGORITHM LGEGA JAISE KI AGR N/2 MAJOPRITY CHIYE TOH 1 HI HOGA SIMILARY N/3 AGR MAJORITY CHIYE TOH 2 HI HOGYE 2N/3 AB TEESRA N/3 SE JYTADA NHI HO SKTA SIMILARY LOGIC EXTENDS AND FOR N/K THERE MUST BE K-1 OR LESS THAN K-1 ELEMNTS
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        cnt1,cnt2 = 0,0
        el1,el2 = float('-inf'),float('-inf')
        #get the maximum occuring elemtns
        for i in range(n):
            if cnt1 == 0 and el2 != nums[i] :
                el1 = nums[i]
                cnt1 += 1
            elif cnt2 == 0 and el1 != nums[i]:
                el2 = nums[i]
                cnt2 += 1
            elif el1 == nums[i]:
                cnt1 += 1
            elif el2 == nums[i]:
                cnt2 += 1
            else :
                cnt1 -= 1
                cnt2 -= 1
        cnt1,cnt2 = 0,0
        for i in range(n):
            if nums[i] == el1 :
                cnt1 += 1
            if nums[i] == el2 :
                cnt2 += 1
        req = math.floor(n/3)
        res = []
        if cnt1 > req :
            res.append(el1)
        if cnt2 > req :
            res.append(el2)
        return res
