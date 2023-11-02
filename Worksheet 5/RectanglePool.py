import Rectangle


class RectanglePool:

    def __init__(self):
        self.rectangles = []

    def addRectange(self, rectangle: Rectangle):
        self.rectangles.append(rectangle)

    def getTotalArea(self):
        total_area = 0
        for rect in self.rectangles:
            total_area += rect.getArea()

        return total_area
