class DetectSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[(x,y)] += 1
            
    def count(self, point: List[int]) -> int:
        x, y = point
        result = 0

        for key in self.points:
            #if the point is diagonal to the current point then we can potentially form a square
            curx, cury = key

            #0. if same point then skip
            if curx == x and cury == y: continue

            #1. Check Diagonal
            if abs(curx - x) != abs(cury - y): continue
            
            #2. Are diagonal so check for other points
            if (curx, y) in self.points and (x, cury) in self.points:
                result += self.points[(curx, cury)] * self.points[(curx, y)] * self.points[(x, cury)]
            
        return result

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)