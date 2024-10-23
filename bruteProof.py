import dudraw
import random

"""
When you run this code, it shows the oritional points with edges connecting where the convex hull points are.
"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __repr__(self):
        return f"Point({self.x}, {self.y})"
        
class Edge(Point):
    def __init__(self, point1, point2):
        super().__init__(point1.x, point1.y)
        self.point1 = point1
        self.point2 = point2

    def __str__(self):
        return f"Edge({self.point1}, {self.point2})"

    def __repr__(self):
        return f"Edge({self.point1}, {self.point2})"

    def draw(self):
        dudraw.line(self.point1.x, self.point1.y, self.point2.x, self.point2.y,)
    
def create_points(nums):
    points = []
    for i in range(nums):
        new_point = Point(random.random(), random.random())
        points.append(new_point)
    return points

def leftTurn(F, M, E):
    return (((M.x - F.x) * (M.y - E.y)) - ((M.y - F.y) * (M.x - E.x))) <= 0
    

points = create_points(50)
# points = [Point(.25,.25), Point(.75,.25), Point(.5,.75), Point(.5,.5)]


for point in points:
    dudraw.filled_circle(point.x, point.y, 0.005)

def bruteHull(points):
    edge_points = []
    for i in range(len(points)):
        for j in range(len(points)):
            if j == i:
                continue
            left_count = 0
            for k in range(len(points)):
                if k == i or k == j:
                    continue
                if leftTurn(points[i],points[j],points[k]):
                    left_count += 1
                
            if left_count == len(points)-2 or left_count == 0:
                new_edge = Edge(points[i],points[j])
                edge_points.append(new_edge)

            
                
    return edge_points        

edges = bruteHull(points)
print(edges)
dudraw.set_pen_color(dudraw.RED)
for edge in edges:
    edge.draw()
dudraw.show(100000)

