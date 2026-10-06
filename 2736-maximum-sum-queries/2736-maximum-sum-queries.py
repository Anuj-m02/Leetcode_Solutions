class Solution:
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        
        pairs = sorted(zip(nums1 , nums2) , reverse=True)

        sorted_queries = sorted(range(len(queries)) , key = lambda i : queries[i][0] , reverse=True)

        ans = [-1]*(len(queries))

        stack = []
        p_indx = 0
        n = len(pairs)

        for q_indx in sorted_queries :
            qx , qy = queries[q_indx]

            while p_indx < n and pairs[p_indx][0] >= qx :
                x , y = pairs[p_indx]
                val = x+y

                while stack and stack[-1][1] <= val :
                    stack.pop()
                
                if not stack or stack[-1][0] < y :
                    stack.append((y , val))
                
                p_indx += 1
            
            indx = bisect.bisect_left(stack , qy , key = lambda item : item[0])
            if indx < len(stack) :
                ans[q_indx] = stack[indx][1]
        
        return ans
