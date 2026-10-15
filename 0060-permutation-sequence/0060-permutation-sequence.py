from itertools import permutations
class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        arr = list(range(1,n+1))
        
        string = ""
        for val in arr :
            string += str(val)
        
        temp = permutations(string)
        a = list(temp)
        
        res = a[k-1]
        ans = ""
        for val in res :
            ans += str(val)

        return ans


        # fact = 1
        # nums = []
        # for i in range(1,n):
        #     fact = fact*i
        #     nums.append(i)
        # nums.append(n)
        # ans = ""
        # k -= 1
        # while True :
        #     ans = ans + str(nums[k//fact])
        #     nums.remove(nums[k//fact])
        #     if len(nums) == 0 :
        #         break
        #     k = k%fact
        #     fact = fact//len(nums)
        # return ans
    
