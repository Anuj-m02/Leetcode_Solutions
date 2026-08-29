class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        n = len(s)

        # dsu = DSU(n)

        graph = defaultdict(list)

        for u , v in pairs :
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [False]*(n)
        res = list(s)

        for i in range(n) :
            if not visited[i] :
                component_indices = []
                queue = deque([i])
                visited[i] = True

                while queue :
                    curr_indx = queue.popleft()

                    component_indices.append(curr_indx)

                    for neighbour in graph[curr_indx] :
                        if not visited[neighbour] :
                            visited[neighbour] = True
                            queue.append(neighbour)
                
                # now for this component sort
                component_chars = [s[indx] for indx in component_indices]
                component_indices.sort()
                component_chars.sort()

                for indx , char in zip(component_indices , component_chars):
                    res[indx] = char
        
        return "".join(res)

        # queue = deque([(s)])

        # vis = {s}
        # mini = s

        # while queue :
        #     curr_string = queue.popleft()
        #     mini = min(mini , curr_string)
        #     temp = list(curr_string)
        #     for indx in range(n) :

        #         for neighbour in graph[indx] :
        #             temp[neighbour] , temp[indx] = temp[indx] , temp[neighbour]
        #             new_str = "".join(temp)

        #             if new_str not in vis :
        #                 vis.add(new_str)
        #                 queue.append((new_str))
        
        # return mini
