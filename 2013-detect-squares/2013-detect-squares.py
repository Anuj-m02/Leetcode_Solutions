from collections import defaultdict , deque , Counter

class DetectSquares:

    def __init__(self):
        self.point_counts = Counter()
        self.points = []


    def add(self, point: list[int]) -> None:
        pt = tuple(point)
        self.point_counts[pt] += 1
        self.points.append(pt)

        

    def count(self, point: list[int]) -> int:

        ans = 0
        px , py = point

        for x,y in self.points :

            if abs(px-x) != abs(py-y) or px == x or py == y :
                continue

            ans += self.point_counts[(px,y)] * self.point_counts[(x,py)]

        return ans 


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)