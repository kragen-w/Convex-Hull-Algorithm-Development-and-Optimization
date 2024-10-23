import dudraw
import random
import math
from time import time

"""
When you run this code, it will begin displaying a table in the console of the timing for brute first, then divide and conqor.
The important column to look at is the runtime colum, as that is the one that shows how long it takes to find the convex
hull of a set of points of size n.
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

def ply_timer(num_trial = int, poly_name = str, function = object, sorted = bool):
    

    #the toops of each column are printed
    print(f"n\t\telapsed_time\t\truntime\t\t\t{poly_name}")
    #n will take on these in a loop
    for n in (50, 60, 70, 80, 90):
        # making the array
        points = create_points(n)
        #the timer is started
        start = time()
        #for however many trials there are...
        for j in range(num_trial):
            #the algorithm is ran
            function(points)
        #the time is stopped
        stop = time()
        #the times are printed
        print(f"{n}\t\t{stop - start}\t{(stop - start)/num_trial}")

        
ply_timer(40, "Brute Force", bruteHull, True)
ply_timer(15000, "Divide and Conquer", QuickStart, False)
