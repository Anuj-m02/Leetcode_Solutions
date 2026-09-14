class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        
        x1 , y1 , x2 , y2 = rec1
        side1 = abs(y1-y2)
        side2 = abs(x1-x2)

        a1 , b1 , a2 , b2 = rec2
        
        x_overlap = min(x2 , a2) > max(x1 , a1)
        y_overlap = min(y2 , b2) > max(y1 , b1)

        return x_overlap and y_overlap