from collections import defaultdict
import heapq
from typing import List


class Solution:

  def findMaxPathScore(
      self, edges: List[List[int]], online: List[bool], k: int
  ) -> int:

    n = len(online)
    graph = defaultdict(list)

    low = float("inf")
    high = -1

    # Filter offline nodes upfront
    for u, v, cost in edges:
      if online[u] and online[v]:
        graph[u].append((v, cost))
        low = min(low, cost)
        high = max(high, cost)

    # Edge case: if low didn't change, no valid edges between online nodes
    if low == float("inf"):
      return -1

    def check(mid):
      # curr_cost , curr_node
      heap = [(0, 0)]
      dist = [float("inf")] * n  # FIXED: initialize with infinity
      dist[0] = 0

      while heap:
        curr_cost, curr_node = heapq.heappop(heap)

        if curr_cost > dist[curr_node]:
          continue

        if curr_node == n - 1:
          return True

        for neighbour, cost in graph[curr_node]:
          if cost >= mid:
            new_cost = curr_cost + cost

            if new_cost <= k and new_cost < dist[neighbour]:
              dist[neighbour] = new_cost
              heapq.heappush(heap, (new_cost, neighbour))

      return False

    ans = -1

    while low <= high:
      mid = (low + high) // 2

      if check(mid):
        low = mid + 1
        ans = mid
      else:
        high = mid - 1

    return ans