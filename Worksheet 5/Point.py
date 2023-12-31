
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __add__(self, other):
        return Point(self.getX()+other.getX(), self.getY()+other.getY())

