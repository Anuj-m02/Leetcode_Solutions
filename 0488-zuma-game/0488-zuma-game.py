from collections import defaultdict , deque , Counter
import heapq
from functools import lru_cache


class Solution:
    def findMinStep(self, board: str, hand: str) -> int:

        n = len(board)
        hand = "".join(sorted(hand))

        def update(board , indx) :
            if indx < 0 :
                return board
            
            left = right = indx

            while left > 0 and board[left] == board[left-1] :
                left -= 1
            while right < len(board) - 1 and board[right] == board[right+1] :
                right += 1

            same_clr_len = right-left+1
            if same_clr_len >= 3 :
                return update(board[:left] + board[right+1 :] , left-1)
            else :
                return board 

        d = defaultdict(int)
        for s in hand :
            d[s] += 1
                        # board , hand , step
        queue = deque([(board , hand , 0)])
        visited = {board + "#" + hand}

        while queue :
            curr_board , curr_hand , curr_step = queue.popleft()

            for i in range(len(curr_board)):
                for j in range(len(curr_hand)) :

                    # # skip duplicate
                    # if j > 0 and curr_hand[j] == curr_hand[j-1] :
                    #     continue
                    # if i > 0 and curr_board[i-1] == curr_hand[j] :
                    #     continue
                    
                    worthTrying = False

                    if curr_board[i] == curr_hand[j] :
                        worthTrying = True
                    elif i > 0 and curr_board[i] == curr_board[i-1] != curr_hand[j] :
                        worthTrying = True
                    
                    if worthTrying :
                        new_board = update(curr_board[:i] + curr_hand[j] + curr_board[i:] , i)

                        if not new_board :
                            return curr_step + 1
                        new_hand = curr_hand[:j] + curr_hand[j+1 : ]

                        state = new_board + "#" + new_hand
                        if state not in visited :
                            visited.add(state)
                            queue.append((new_board , new_hand , curr_step+1))
            
        return -1

