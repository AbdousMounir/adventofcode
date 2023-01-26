from enum import Enum


class Limit(object):
    def __init__(self, startPosition, endPosition, orientation):
        self.startPosition = startPosition
        self.endPosition = endPosition
        self.orientation = orientation


class Point(object):
    def __init__(self, x, y):
        self.X = int(x)
        self.Y = int(y)


class PositionType(Enum):
    Empty = " "
    Road = "."
    Wall = "#"


transitionsDemo = [
    (Limit(Point(2, 0), Point(3, 0), Point(0, -1)),
     Limit(Point(1, 1), Point(0, 1), Point(0, -1))),
    (Limit(Point(3, 0), Point(3, 1), Point(1, 0)),
     Limit(Point(4, 3), Point(4, 2), Point(1, 0))),
    (Limit(Point(3, 1), Point(3, 2), Point(1, 0)),
     Limit(Point(4, 2), Point(3, 2), Point(0, -1))),
    (Limit(Point(3, 3), Point(4, 3), Point(0, 1)),
     Limit(Point(0, 2), Point(1, 2), Point(-1, 0))),
    (Limit(Point(2, 3), Point(3, 3), Point(0, 1)),
     Limit(Point(1, 2), Point(0, 2), Point(0, 1))),
    (Limit(Point(2, 2), Point(2, 3), Point(-1, 0)),
     Limit(Point(2, 2), Point(1, 2), Point(0, 1))),
    (Limit(Point(1, 1), Point(2, 1), Point(0, -1)),
     Limit(Point(2, 0), Point(2, 1), Point(-1, 0)))
]

transitions = [
    (Limit(Point(1, 0), Point(2, 0), Point(0, -1)),
     Limit(Point(0, 3), Point(0, 4), Point(-1, 0))),
    (Limit(Point(2, 0), Point(3, 0), Point(0, -1)),
     Limit(Point(0, 4), Point(1, 4), Point(0, 1))),
    (Limit(Point(3, 0), Point(3, 1), Point(1, 0)),
     Limit(Point(2, 3), Point(2, 2), Point(1, 0))),
    (Limit(Point(2, 1), Point(3, 1), Point(0, 1)),
     Limit(Point(2, 1), Point(2, 2), Point(1, 0))),
    (Limit(Point(1, 3), Point(2, 3), Point(0, 1)),
     Limit(Point(1, 3), Point(1, 4), Point(1, 0))),
    (Limit(Point(0, 2), Point(0, 3), Point(-1, 0)),
     Limit(Point(1, 1), Point(1, 0), Point(-1, 0))),
    (Limit(Point(0, 2), Point(1, 2), Point(0, -1)),
     Limit(Point(1, 1), Point(1, 2), Point(-1, 0)))
]
