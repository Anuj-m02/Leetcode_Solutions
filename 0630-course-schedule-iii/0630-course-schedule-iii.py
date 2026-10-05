class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        
        n = len(courses)

        courses.sort(key = lambda x : x[1])

        max_heap = []
        total_time = 0

        for duration , last_day in courses :

            total_time += duration
            heapq.heappush(max_heap , -duration)

            if total_time > last_day :
                longest_duration = -heapq.heappop(max_heap)
                total_time -= longest_duration
        
        return len(max_heap)
