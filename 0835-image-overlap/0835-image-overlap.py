from collections import Counter
from typing import List

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        
        # 1. Collect coordinates of 1s in both images
        p1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        p2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]
        
        # 2. Count frequencies of all shift vectors (r2 - r1, c2 - c1)
        shift_counts = Counter((r2 - r1, c2 - c1) for r1, c1 in p1 for r2, c2 in p2)
        
        # 3. The answer is the highest frequency of any shift vector
        return max(shift_counts.values(), default=0)