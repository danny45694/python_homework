import math

class Point:
    def __init__(self, x: float, y: float):
        self.x = float(x)
        self.y = float(y)

    def __repr__(self) -> str:
        return f"Point(x={self.x}, y={self.y})"

    def __str__(self) -> str:
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other) -> bool:
        if isinstance(other, Point):
            return (self.x, self.y) == (other.x, other.y)
        return NotImplemented

    def distance_to(self, other: "Point") -> float:
        return math.hypot(self.x - other.x, self.y - other.y)


class Vector(Point):
    def __init__(self, x: float, y: float):
        super().__init__(x, y)

    def __str__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented


# 🔎 Test/demo section
if __name__ == "__main__":
    p1 = Point(2, 3)
    p2 = Point(2, 3)
    p3 = Point(5, 7)
    v1 = Vector(1, 1)
    v2 = Vector(2, 3)

    print("Testing Points:")
    print(p1)                        # Point(2.0, 3.0)
    print(p1 == p2)                  # True
    print(p1 == p3)                  # False
    print(f"Distance from p1 to p3: {p1.distance_to(p3)}")  # ~5.0

    print("\nTesting Vectors:")
    print(v1)                        # Vector(1.0, 1.0)
    print(v2)                        # Vector(2.0, 3.0)
    v3 = v1 + v2
    print(f"v1 + v2 = {v3}")         # Vector(3.0, 4.0)
