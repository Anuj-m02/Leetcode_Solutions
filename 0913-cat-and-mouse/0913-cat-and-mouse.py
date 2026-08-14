from collections import deque
from typing import List

class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)
        
        # Outcomes: 0 = DRAW, 1 = MOUSE WINS, 2 = CAT WINS
        # color[m][c][turn]
        color = [[[0] * 2 for _ in range(n)] for _ in range(n)]
        
        # degree[m][c][turn] stores the number of available valid moves from this state
        degree = [[[0] * 2 for _ in range(n)] for _ in range(n)]
        
        # Calculate out-degrees for every valid state
        for m in range(n):
            for c in range(n):
                # Mouse's turn: Mouse can move to any neighbor in graph[m]
                degree[m][c][0] = len(graph[m])
                
                # Cat's turn: Cat can move to any neighbor in graph[c] EXCEPT hole (0)
                degree[m][c][1] = len(graph[c]) - (1 if 0 in graph[c] else 0)
        
        queue = deque()
        
        # 1. Enqueue all base terminal states
        for i in range(1, n):
            for turn in range(2):
                # Mouse reaches hole (0) -> Mouse Wins (1)
                color[0][i][turn] = 1
                queue.append((0, i, turn, 1))
                
                # Cat catches Mouse -> Cat Wins (2)
                color[i][i][turn] = 2
                queue.append((i, i, turn, 2))
        
        # Helper function to find parent states (previous turns)
        def get_parents(m: int, c: int, turn: int):
            parents = []
            if turn == 0:
                # If current turn is Mouse's (0), parent turn was Cat's (1)
                for prev_c in graph[c]:
                    if prev_c != 0:  # Cat could never have been at the hole
                        parents.append((m, prev_c, 1))
            else:
                # If current turn is Cat's (1), parent turn was Mouse's (0)
                for prev_m in graph[m]:
                    parents.append((prev_m, c, 0))
            return parents

        # 2. Process Queue (Reverse BFS)
        while queue:
            m, c, turn, result = queue.popleft()
            
            for pm, pc, pturn in get_parents(m, c, turn):
                # Skip if parent state outcome is already determined
                if color[pm][pc][pturn] != 0:
                    continue
                
                # Check if the parent state's active player can force a win
                if pturn == 0 and result == 1:
                    # Mouse's turn in parent state, and this move leads to Mouse Win
                    color[pm][pc][pturn] = 1
                    queue.append((pm, pc, pturn, 1))
                elif pturn == 1 and result == 2:
                    # Cat's turn in parent state, and this move leads to Cat Win
                    color[pm][pc][pturn] = 2
                    queue.append((pm, pc, pturn, 2))
                else:
                    # Current move is bad for parent player; decrement degree of available choices
                    degree[pm][pc][pturn] -= 1
                    
                    # If ALL moves from parent state lead to opponent winning:
                    if degree[pm][pc][pturn] == 0:
                        # If Mouse has no non-losing options, Cat wins (2)
                        # If Cat has no non-losing options, Mouse wins (1)
                        loser_result = 2 if pturn == 0 else 1
                        color[pm][pc][pturn] = loser_result
                        queue.append((pm, pc, pturn, loser_result))
                        
        # Initial starting state: Mouse at 1, Cat at 2, Mouse moves first (turn = 0)
        return color[1][2][0]