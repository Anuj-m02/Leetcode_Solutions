class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        

        # poss = 2345 , 4567 , 6789

        m = len(reservedSeats)
        rows_reserved = set()
        for i in range(m) :
            rows_reserved.add(reservedSeats[i][0])

        each_row_dict = defaultdict(list)
        for i in range(m) :
            curr_row , curr_seat = reservedSeats[i][0] , reservedSeats[i][1]
            each_row_dict[curr_row].append(curr_seat)

        cnt = 0
        grps = [(2 , 3 , 4 , 5) , (4 , 5 , 6 , 7) , (6 , 7, 8, 9)]
        for rows in each_row_dict :
            seats_booked = each_row_dict[rows]
            left_ok = not (2 in seats_booked or 3 in seats_booked or 4 in seats_booked or 5 in seats_booked)
            right_ok = not (6 in seats_booked or 7 in seats_booked or 8 in seats_booked or 9 in seats_booked)
            mid_ok = not (4 in seats_booked or 5 in seats_booked or 6 in seats_booked or 7 in seats_booked)

            if left_ok and right_ok :
                cnt += 2
            elif left_ok or right_ok or mid_ok :
                cnt += 1
        
        left_rows = n - len(rows_reserved)
        cnt += 2*(left_rows)
        
        return cnt







