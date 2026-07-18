class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        
        res = [0]*(n+1)

        for i in range(len(bookings)) :
            left , right , num = bookings[i]

            res[left-1] += num
            res[right] -= num

        for i in range(1,n):
            res[i] += res[i-1]
        
        return res[:n]
