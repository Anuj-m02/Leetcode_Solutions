class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        
        n = len(nums)
        num_digits = len(str(nums[0]))

        # _ _ _ _ _ _ _ _ _ 1e9 nums[i]
        # at each pos cnt of [0][1][2][3]..[9] for pos1 ,[0][1][2][3]..[9] for pos2

        d = defaultdict(list)

        for pos in range(num_digits) :
            cnt_arr = [0]*(10)
            d[pos] = cnt_arr
            for digit in range(10) :
                for num_indx in range(n) :
                    s = str(nums[num_indx])
                    if int(s[pos]) == digit :
                        d[pos][digit] += 1
        
        diff = 0
        for pos in range(num_digits) :
            cnt_arr = d[pos]

            for digit in range(10) :
                c = cnt_arr[digit]
                diff += c*(n-c)
        
        return diff//2
                



