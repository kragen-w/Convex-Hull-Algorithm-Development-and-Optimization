import dudraw
import random
import math

"""
When you run this code, it shows the origional points for a second, then it shows the convex hull points overlayed in red.
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __repr__(self):
        return f"Point({self.x}, {self.y})"
    
    def draw(self):
        dudraw.filled_circle(self.x, self.y, 0.005)
        
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

def crossProduct(F, M, E):
    return (((M.x - F.x) * (M.y - E.y)) - ((M.y - F.y) * (M.x - E.x)))
    

points = create_points(50)
# points = [Point(.25,.25), Point(.75,.25), Point(.5,.75), Point(.5,.5)]




def QuickStart(points):
    edge_points = []

    b = points[0]
    a = points[0]
    for point in points:
        if b.x < point.x:
            b = point
        if a.x > point.x:
            a = point
    edge_points.append(a)
    edge_points.append(b)
    upper = []
    lower = []
    for point in points:
        if point == a or point == b:
            continue
        if leftTurn(a,b,point):
            upper.append(point)
        else:
            lower.append(point)
    upper_hull = QuickHull(a,b,upper, edge_points)
    lower_hull = QuickHull(b,a,lower, edge_points)
    return edge_points


def QuickHull(a, b, points, edge_points):
    if len(points) <= 1:
        for i in range(len(points)):
            edge_points.append(points[i])
            return
    c_distance = 0
    for point in points:
        if abs(crossProduct(a,b,point)) > c_distance:
            c_point = point
            c_distance = abs(crossProduct(a,b,point))
    if c_distance == 0:
        return
    A = []
    B = []
    for point in points:
        if leftTurn(a, c_point, point):
            A.append(point)
        if leftTurn(c_point,b,point):
            B.append(point)
    if len(A) == 0 and len(B) == 0:
        edge_points.append(c_point)
        return
    edge_points.append(c_point)
    QuickHull(a,c_point,A, edge_points)
    QuickHull(c_point,b,B, edge_points)
    return
    
for point  in points:
    point.draw()
dudraw.show(1000)

edge_p = QuickStart(points)

dudraw.set_pen_color(dudraw.RED)
for p in edge_p:
    p.draw()
dudraw.show(10000000)



