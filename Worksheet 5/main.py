from Point import Point
from Rectangle import Rectangle
from RectanglePool import RectanglePool
from TicTacToe import TicTacToe

# 1)

p1 = Point(1, 1)
p2 = Point(6, 6)

rect1 = Rectangle(p1, p2)

p3 = Point(5, 5)
p4 = Point(15, 15)

rect2 = Rectangle(p3, p4)

rect_pool = RectanglePool()
rect_pool.addRectange(rect1)
rect_pool.addRectange(rect2)

print(rect1)
print(rect1.getArea())
print(rect2)
print(rect2.getArea())
print(rect1.getArea() + rect2.getArea())
print(rect_pool.getTotalArea())

print([x for x in range(2, -1, -1)])

# 2)

game = TicTacToe()
game.printBoard()

while not game.isFinished():
    (row, col) = input("Enter the row and column for your move with no overlap eg: (0 0): ").split(" ")
    row = int(row)
    col = int(col)
    try:
        game.playPlayerTurn(row, col)
    except Exception as e:
        print(e)

    game.printBoard()