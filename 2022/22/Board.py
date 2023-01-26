from utils import PositionType, Point


class Board(object):
    def __init__(self, board):
        self.initialData = board
        self.maxHeight = len(board)
        self.maxWidth = len(max(board, key=len))
        self.orientation = Point(1, 0)
        self.position = self.createPosition()
        self.currentPosition = self.getStartingPosition()

    def __str__(self):
        return self.initialData.join('\n')

    def createPosition(self):
        position = {}
        for y, row in enumerate(self.initialData):
            for x, value in enumerate(row):
                position[(x, y)] = value
            x += 1
            while x < self.maxWidth:
                position[(x, y)] = PositionType.Empty.value
                x += 1
        return position

    def getStartingPosition(self):
        x = 0
        while x < self.maxWidth:
            if (self.position[x, 0] == PositionType.Road.value):
                return Point(x, 0)
            else:
                x += 1

    def applyMovements(self, path):
        for movement in path:
            if (movement == "R"):
                self.orientation = Point(-self.orientation.Y,
                                         self.orientation.X)
            elif (movement == "L"):
                self.orientation = Point(
                    self.orientation.Y, -self.orientation.X)
            else:
                self.getNextPosition(movement)

    def getNextPosition(self, movement):
        for _ in range(int(movement)):
            nextPosition = Point(self.currentPosition.X,
                                 self.currentPosition.Y)
            notFound = True
            while notFound:
                nextPosition = Point(
                    (nextPosition.X + self.orientation.X) % self.maxWidth,
                    (nextPosition.Y + self.orientation.Y) % self.maxHeight
                )
                boardNextPosition = self.position[nextPosition.X,
                                                  nextPosition.Y]

                if (boardNextPosition == PositionType.Road.value):
                    notFound = False
                if (boardNextPosition == PositionType.Wall.value):
                    return
            self.currentPosition = nextPosition

    def getAwnser(self):
        orientationPoints = 0
        if (self.orientation.X == 0):
            if (self.orientation.Y == -1):
                orientationPoints = 3
            else:
                orientationPoints = 1
        if (self.orientation.Y == 0):
            if (self.orientation.X == -1):
                orientationPoints = 2

        return int(1000 * (self.currentPosition.Y + 1) + 4 * (self.currentPosition.X + 1) + orientationPoints)
