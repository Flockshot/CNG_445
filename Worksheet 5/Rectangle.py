import Point


class Rectangle:

    def __init__(self, t: Point, b: Point):
        self.topLeft = t
        self.bottomRight = b

    def getArea(self):
        length = abs(self.topLeft.getX() - self.bottomRight.getX())
        width = abs(self.topLeft.getY() - self.bottomRight.getY())
        return length * width

    def __str__(self):
        return "[({},{}) ({}, {})]".format(self.topLeft.getX(), self.topLeft.getY(), self.bottomRight.getX(),
                                           self.bottomRight.getY())

    def __add__(self, other):
        return Rectangle(self.topLeft + other.topLeft, self.bottomRight + other.bottomRight)
