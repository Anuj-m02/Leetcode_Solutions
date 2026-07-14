class Solution:
    def minimumCost(self, nums: list[int], k: int) -> int:
        
        mod = int(1e9)+7
        n = len(nums)
        cnt = 0
        k_org = k
        for i in range(n):
            curr = nums[i]
            if k >= curr :
                k -= curr
            else :
                need = math.ceil((curr-k)/k_org)

                k += need*k_org
                cnt += need
                k -= curr


                # while k < curr :
                #     k += k_org
                #     cnt += 1
                # k -= curr
            # print(k)
            # print(cnt)
        
        return (cnt*(cnt+1)//2)%mod
            




        