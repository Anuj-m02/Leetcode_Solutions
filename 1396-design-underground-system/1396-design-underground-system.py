class UndergroundSystem:

    def __init__(self):

        self.user_to_station = {}
        # user_id : (station chekcin , checkin time)
        self.station_to_station = {}
        # (station a , station b) : [total time , trip count]
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:

        self.user_to_station[id] = (stationName , t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:

        start_station , check_in_time = self.user_to_station.pop(id)

        trip_duration = t - check_in_time
        route_key = (start_station , stationName)

        if route_key in self.station_to_station :
            self.station_to_station[route_key][0] += trip_duration
            self.station_to_station[route_key][1] += 1
        
        else :
            self.station_to_station[route_key] = [trip_duration , 1]
    

        

    def getAverageTime(self, startStation: str, endStation: str) -> float:

        total_time , trip_count = self.station_to_station[(startStation , endStation)] 

        return total_time / trip_count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)