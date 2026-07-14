class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        end_time = int(endTime[0:2])*3600 + int(endTime[3:5])*60 + int(endTime[6:])
        start_time = int(startTime[0:2])*3600 + int(startTime[3:5])*60 + int(startTime[6:])

        return end_time - start_time