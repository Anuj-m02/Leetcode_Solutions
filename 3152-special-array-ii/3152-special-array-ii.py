class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        

        n = len(nums)

        prefix = [0]*(n)

        for i in range(1 , n) :
            prefix[i] = prefix[i-1]

            if (nums[i-1] % 2 == 0 and nums[i] % 2 == 0 ) or (nums[i-1] % 2 == 1 and nums[i]%2 == 1) :
                prefix[i] += 1
        
        res = []

        for left , right in queries :
            cnt = prefix[right] - (prefix[left] if left > 0 else 0)
            res.append(cnt == 0)
        
        return res


        # 1 1 2 2 2

