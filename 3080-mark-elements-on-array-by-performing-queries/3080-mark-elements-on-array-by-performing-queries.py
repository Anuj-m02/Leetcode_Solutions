class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        

        n = len(nums)
        total = sum(nums)

        not_vis = set(range(n))
        ans = []

        heap = []
        for indx , val in enumerate(nums) :
            heap.append((val , indx))
        
        heapq.heapify(heap)

        for indx , k in queries :

            if indx in not_vis :
                total -= nums[indx]
                not_vis.discard(indx)
            

            while k and heap :

                num , indx = heapq.heappop(heap)

                if indx in not_vis :
                    not_vis.discard(indx)
                    k -= 1
                    total -= num
            
            ans.append(total)
        
        return ans
