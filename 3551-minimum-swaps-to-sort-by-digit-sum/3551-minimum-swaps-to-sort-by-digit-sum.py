class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        
        n = len(nums)

        arr = []
        for indx , val in enumerate(nums) :
            d_sum = sum(int(digit) for digit in str(val))
            arr.append((d_sum , val , indx))
        
        # digit_sum,  value
        arr.sort()

        visited = [False]*(n)
        swaps = 0

        for i in range(n) :

            if visited[i] or arr[i][2] == i :
                continue
            
            cycle_size = 0
            curr = i

            while not visited[curr] :
                visited[curr] = True
                curr = arr[curr][2]
                cycle_size += 1
            
            if cycle_size > 0 :
                swaps += (cycle_size-1)
        
        return swaps