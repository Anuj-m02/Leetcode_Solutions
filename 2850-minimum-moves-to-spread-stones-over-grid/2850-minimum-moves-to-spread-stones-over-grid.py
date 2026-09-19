class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        
        zeros = []
        extra = []

        for r in range(3) :
            for c in range(3) :
                if grid[r][c] == 0 :
                    zeros.append((r,c))
                elif grid[r][c] > 1 :
                    for _ in range(grid[r][c]-1) :
                        extra.append((r,c))
        
        @cache
        def dp(empty_indx , used_extra):

            if empty_indx == len(zeros) :
                return 0
            
            zr,zc = zeros[empty_indx]
            min_moves = float("inf")

            for i , (er,ec) in enumerate(extra) :
                if i not in used_extra :
                    moves = abs(zr-er) + abs(zc-ec)
                    nxt_used = used_extra | frozenset([i])

                    min_moves = min(min_moves , moves + dp(empty_indx+1 , nxt_used))
            
            return min_moves
        
        return dp(0 , frozenset())


# from functools import cache

# class Solution:
#     def minimumMoves(self, grid: list[list[int]]) -> int:
#         zeroes = []
#         extras = []
        
#         for r in range(3):
#             for c in range(3):
#                 if grid[r][c] == 0:
#                     zeroes.append((r, c))
#                 elif grid[r][c] > 1:
#                     for _ in range(grid[r][c] - 1):
#                         extras.append((r, c))

#         @cache
#         def backtrack(empty_idx: int, used_extras: frozenset[int]) -> int:
#             if empty_idx == len(zeroes):
#                 return 0
            
#             zr, zc = zeroes[empty_idx]
#             min_moves = float('inf')
            
#             for i, (er, ec) in enumerate(extras):
#                 if i not in used_extras:
#                     moves = abs(zr - er) + abs(zc - ec)
#                     next_used = used_extras | frozenset([i])
                    
#                     min_moves = min(min_moves, moves + backtrack(empty_idx + 1, next_used))
                    
#             return min_moves

#         return backtrack(0, frozenset())