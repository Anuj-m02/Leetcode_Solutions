class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:


        closest_x = max(x1 , min(xCenter , x2))
        closest_y = max(y1 , min(yCenter , y2))

        dx = xCenter - closest_x
        dy = yCenter - closest_y

        return (dx*dx + dy*dy) <= (radius*radius)