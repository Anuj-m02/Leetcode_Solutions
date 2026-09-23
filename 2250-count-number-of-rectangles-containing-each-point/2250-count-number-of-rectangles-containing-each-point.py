class Solution:
    def countRectangles(self, rectangles: list[list[int]], points: list[list[int]]) -> list[int]:
        
        n , m = len(rectangles) , len(points)

        # group length by height
        height_to_length = defaultdict(list)
        for l , h in rectangles :
            height_to_length[h].append(l)
        
        # sort length for each height h 
        for h in height_to_length :
            height_to_length[h].sort()
        
        ans = []
        for x,y in points :

            cnt = 0

            for h in range(y , 101) :
                if h in height_to_length :
                    lengths = height_to_length[h]

                    indx = bisect.bisect_left(lengths , x)
                    cnt += len(lengths) - indx
            
            ans.append(cnt)
        
        return ans
