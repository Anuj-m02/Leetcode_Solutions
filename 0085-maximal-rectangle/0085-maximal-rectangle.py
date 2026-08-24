from collections import defaultdict , deque , Counter
import heapq
from functools import lru_cache


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        n , m = len(matrix) , len(matrix[0])
        heights = [0]*(m)
        max_area = 0

        def area(heights) :
            stack = []
            max_area = 0
            heights.append(0)
            for i , h in enumerate(heights) :
                while stack and heights[stack[-1]] > h :
                    height = heights[stack.pop()]
                    width = i if not stack else i-stack[-1]-1
                    max_area = max(max_area , height*width)
                stack.append(i)
                # print(stack)
            
            heights.pop()
            return max_area

        for row in range(n) :
            for col in range(m) :
                if matrix[row][col] == "1" :
                    heights[col] += 1
                else :
                    heights[col] = 0
            
            max_area = max(max_area , area(heights))
        
        return max_area
