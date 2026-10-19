class Solution:
    def smallestMissingValueSubtree(self, parents: list[int], nums: list[int]) -> list[int]:
        
        n = len(nums)
        ans = [1]*(n)

        graph = defaultdict(list)
        for i in range(1 , n) :
            graph[parents[i]].append(i)

        if 1 not in nums :
            return ans

        visited = [False]*(n)
        seen_values = set()

        def dfs(node) :
            if visited[node] :
                return

            visited[node] = True
            seen_values.add(nums[node])
            for child in graph[node] :
                dfs(child)

        curr = nums.index(1)
        miss = 1

        while curr != -1 :
            dfs(curr) 

            while miss in seen_values :
                miss += 1
            
            ans[curr] = miss
            curr = parents[curr]
        
        return ans
