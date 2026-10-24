# class Solution:
#     def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:

#         days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
#         def date_to_day(date_str) :
#             month , day = map(int , date_str.split("-"))
#             return sum(days_in_months[:month-1]) + day

#         if leaveAlice < arriveBob :
#             return 0
        
#         if leaveBob < arriveAlice :
#             return 0
        
#         mini_arrival , mini_depart = min(arriveAlice , arriveBob) , min(leaveAlice , leaveBob)



class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def date_to_day(date_str: str) -> int:
            month, day = map(int, date_str.split('-'))
            return sum(days_in_months[:month - 1]) + day

        # Overlap starts at the latest arrival and ends at the earliest departure
        start_date = max(arriveAlice, arriveBob)
        end_date = min(leaveAlice, leaveBob)

        # Convert to day numbers
        start_day = date_to_day(start_date)
        end_day = date_to_day(end_date)

        # If the start day is after the end day, there is no overlap
        if start_day > end_day:
            return 0

        # Inclusive difference (+1)
        return end_day - start_day + 1