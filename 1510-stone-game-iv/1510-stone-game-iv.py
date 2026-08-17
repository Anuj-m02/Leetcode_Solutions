# class Solution:
#     def winnerSquareGame(self, n: int) -> bool:
        
#         sq_nums = set()
#         for i in range(1 , int(n** 0.5) + 1) :
#             sq_nums.add(i**2)
        
#         @lru_cache(maxsize=None)
#         def dp(num , turn) :

#             if num == 0 :
#                 if turn == 0 :
#                     return True
#                 return False
            
#             ans = 0
#             if turn == 0 :
#                 for choices in sq_nums :
#                     if choices <= num :
#                         if not dp(num-choices , 1-turn) :
#                             return True
#                 return False

#             else :
#                 for choices in sq_nums :
#                     if choices <= num :
#                         if dp(num-choices , 1-turn) :
#                             return True
#                 return False
                 
            
        
#         return dp(n , 0)


from functools import lru_cache

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
        sq_nums = [i**2 for i in range(1, int(n**0.5) + 1)]
        
        @lru_cache(maxsize=None)
        def dp(num: int, turn: int) -> bool:

            # BASE CASE FIX: 
            # 0 stones left means the CURRENT player loses.
            if num == 0:
                return turn == 1  # If it's Bob's turn (1), Alice won! If Alice's turn (0), Alice lost!

            if turn == 0:  
                # Alice's turn: Alice wants to WIN.
                # If ANY move leads to an Alice victory (dp == True), she takes it.
                for choices in sq_nums:
                    if choices <= num:
                        if dp(num - choices, 1):  # Alice wins in this branch
                            return True
                return False  # Alice loses if no moves lead to a win

            else:  
                # Bob's turn: Bob wants Alice to LOSE.
                # If Bob finds ANY move where Alice loses (dp == False), Bob WILL pick it.
                for choices in sq_nums:
                    if choices <= num:
                        if not dp(num - choices, 0):  # Bob makes a move where Alice loses
                            return False
                return True  # Bob couldn't stop Alice from winning
                 
        return dp(n, 0)