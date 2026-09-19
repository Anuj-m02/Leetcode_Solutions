# # from collections import defaultdict , deque , Counter
# # import heapq
# # from functools import lru_cache


# # class Solution:
# #     def supersequences(self, words: List[str]) -> List[List[int]]:
        
# #         n = len(words)

# #         nodes = set()
# #         edges = set()
# #         for u,v in words :
# #             nodes.add(u)
# #             nodes.add(v)
# #             if u != v :
# #                 edges.add((u,v))
        
# #         nodes_list = sorted(list(nodes))

# #         def is_dag(dup_set) :
# #             single_nodes = nodes - dup_set
# #             graph = defaultdict(list)
# #             indegree = {c : 0 for c in single_nodes}

# #             for u,v in edges :
# #                 if u in single_nodes and v in single_nodes :
# #                     graph[u].append(v)
# #                     indegree[v] += 1
            
# #             queue = deque([c for c in single_nodes if indegree[c] == 0])
# #             processed = 0

# #             while queue :
# #                 curr = queue.popleft()
# #                 processed += 1
# #                 for nxt in graph[curr] :
# #                     indegree[nxt] -= 1
# #                     if indegree[nxt] == 0 :
# #                         queue.append(nxt)
            
# #             return processed == len(single_nodes)


# #         min_dup_sets = []
# #         for k in range(len(nodes_list) + 1) :
# #             for combo in combinations(nodes_list , k) :
# #                 dup_set = frozenset(combo)
# #                 if is_dag(dup_set) :
# #                     min_dup_set.append(dup_set)
            
# #             if min_dup_sets :
# #                 break
        
# #         ans = []
# #         for dup_set in min_dup_sets :
# #             freq = [0]*26
# #             for char in nodes :
# #                 indx = ord(char) - ord("a")
# #                 freq[indx] = 2 if char in dup_set else 1
# #             ans.append(freq)
        
# #         return ans




# #         # graph = defaultdict(list)
# #         # indegree = [0]*(26)
# #         # ans = ""
# #         # for string in words :
# #         #     queue = deque([])
# #         #     first , second = string
# #         #     graph[first].append(second)
# #         #     indegree[second] += 1
        
# #         #     for chars in range(26) :
# #         #         if indegree[char] == 0 :
# #         #             queue.append(char)
            
# #         #     while queue :
# #         #         curr_char = queue.popleft()
# #         #         ans += chr(curr_char+ord("a"))

# #         #         for neighbour in graph[chr(curr_char)] :
# #         #             indegree[neighbour] -= 1
# #         #             if indegree[neighbour] == 0 :
# #         #                 queue.append(ord(neighbour) - ord("a"))
        
# #         # return ans

# from collections import defaultdict, deque
# from itertools import combinations
# from typing import List

# class Solution:
#     def supersequences(self, words: List[str]) -> List[List[int]]:
#         # 1. Collect nodes and directed edges
#         nodes = set()
#         edges = set()
#         for u, v in words:
#             nodes.add(u)
#             nodes.add(v)
#             if u != v:
#                 edges.add((u, v))

#         nodes_list = sorted(list(nodes))

#         # Helper to check if single-occurrence nodes form an acyclic graph (DAG)
#         def is_dag(dup_set: frozenset) -> bool:
#             single_nodes = nodes - dup_set
#             adj = defaultdict(list)
#             indegree = {c: 0 for c in single_nodes}

#             for u, v in edges:
#                 if u in single_nodes and v in single_nodes:
#                     adj[u].append(v)
#                     indegree[v] += 1

#             queue = deque([c for c in single_nodes if indegree[c] == 0])
#             processed = 0

#             while queue:
#                 curr = queue.popleft()
#                 processed += 1
#                 for nxt in adj[curr]:
#                     indegree[nxt] -= 1
#                     if indegree[nxt] == 0:
#                         queue.append(nxt)

#             return processed == len(single_nodes)

#         # 2. Test combinations of duplicated sets of increasing size
#         min_dup_sets = []
#         for k in range(len(nodes_list) + 1):
#             for combo in combinations(nodes_list, k):
#                 dup_set = frozenset(combo)
#                 if is_dag(dup_set):
#                     min_dup_sets.append(dup_set)
            
#             # The first non-empty size k is guaranteed to be the minimum length
#             if min_dup_sets:
#                 break

#         # 3. Build frequency vectors (length 26)
#         ans = []
#         for dup_set in min_dup_sets:
#             freq = [0] * 26
#             for char in nodes:
#                 idx = ord(char) - ord('a')
#                 freq[idx] = 2 if char in dup_set else 1
#             ans.append(freq)

#         return ans
from collections import defaultdict, deque
from itertools import combinations
from typing import List

class Solution:
    def supersequences(self, words: List[str]) -> List[List[int]]:
        nodes = set()
        edges = set()
        must_dup = set()  # Characters that MUST appear twice due to "aa", "bb", etc.

        for u, v in words:
            nodes.add(u)
            nodes.add(v)
            if u == v:
                must_dup.add(u)
            else:
                edges.add((u, v))

        nodes_list = sorted(list(nodes))

        # Check if single-occurrence nodes form a valid DAG (Kahn's Algorithm)
        def is_dag(dup_set: frozenset) -> bool:
            single_nodes = nodes - dup_set
            graph = defaultdict(list)
            indegree = {c: 0 for c in single_nodes}

            for u, v in edges:
                if u in single_nodes and v in single_nodes:
                    graph[u].append(v)
                    indegree[v] += 1

            queue = deque([c for c in single_nodes if indegree[c] == 0])
            processed = 0

            while queue:
                curr = queue.popleft()
                processed += 1
                for nxt in graph[curr]:
                    indegree[nxt] -= 1
                    if indegree[nxt] == 0:
                        queue.append(nxt)

            return processed == len(single_nodes)

        # Iterate over size k of duplicated characters
        min_dup_sets = []
        for k in range(len(must_dup), len(nodes_list) + 1):
            for combo in combinations(nodes_list, k):
                dup_set = frozenset(combo)
                
                # Must contain all self-loop characters ("aa", "bb")
                if not must_dup.issubset(dup_set):
                    continue

                if is_dag(dup_set):
                    min_dup_sets.append(dup_set)

            if min_dup_sets:
                break

        # Convert valid duplicated sets to size 26 frequency arrays
        ans = []
        for dup_set in min_dup_sets:
            freq = [0] * 26
            for char in nodes:
                idx = ord(char) - ord('a')
                freq[idx] = 2 if char in dup_set else 1
            ans.append(freq)

        return ans