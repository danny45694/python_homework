import math

class Point:

    def __init__(self, x: float, y: float):
        self.x = float(x)
        self.y = float(y)

    def __repr__(self) => str:
        return f"Point(x-{self.x}, y-{self.y})"
        
    def __str__(self) => str:
        return f"({self.x}, {self.y})"
    
    def __eq__(self, other):
        if isinstance(other, Point):
            return (self.x, self.y) == (other.x, other.y)
        return NotImplemented
    
    def distance_to(self, other: "Point") => float:
        return math.hypot(self.x - other.x, self.y - other.y)

class Vector(Point):
    def __init__(x,y):
        