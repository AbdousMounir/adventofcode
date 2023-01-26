from Board import Board
from utils import PositionType, Point


class Cube(Board):
    def __init__(self, board, scale, transitions):
        super().__init__(board)
        self.scale = scale
        self.transitions = transitions

    def getNextPosition(self, movement):
        for _ in range(int(movement)):
            nextPosition, nextOrientation = self.verifyTransitions()
            if (nextPosition == None):
                nextPosition = Point(
                    (self.currentPosition.X + self.orientation.X),
                    (self.currentPosition.Y + self.orientation.Y)
                )
            boardNextPosition = self.position[nextPosition.X, nextPosition.Y]

            if (boardNextPosition == PositionType.Wall.value):
                return

            self.currentPosition = nextPosition
            if (nextOrientation != None):
                self.orientation = nextOrientation

    def verifyTransitions(self):
        for transition in self.transitions:
            nextPosition, nextOrientation = self.checkLimit(
                transition[0], transition[1])
            if (nextPosition == None):
                nextPosition, nextOrientation = self.checkLimit(
                    transition[1], transition[0])
            if (nextPosition != None):
                return nextPosition, nextOrientation
        return None, None

    def checkLimit(self, fromLimit, toLimit):
        fromStartPosition, fromEndPosition, fromReversed = self.getScaledPositions(
            fromLimit)

        if (
            (
                (fromStartPosition.X <= self.currentPosition.X <= fromEndPosition.X)
                or (fromStartPosition.X == self.currentPosition.X == fromEndPosition.X)
            )
            and (
                (fromStartPosition.Y <= self.currentPosition.Y <= fromEndPosition.Y)
                or (fromStartPosition.Y == self.currentPosition.Y == fromEndPosition.Y)
            )
            and fromLimit.orientation.X == self.orientation.X
            and fromLimit.orientation.Y == self.orientation.Y
        ):
            toStartPosition, toEndPosition, toReversed = self.getScaledPositions(
                toLimit)

            if (fromStartPosition.X == fromEndPosition.X):
                diff = self.currentPosition.Y - fromStartPosition.Y
            elif (fromStartPosition.Y == fromEndPosition.Y):
                diff = self.currentPosition.X - fromStartPosition.X

            if (toStartPosition.X == toEndPosition.X):
                newX = toStartPosition.X
                if (
                    (toReversed and not fromReversed)
                    or (not toReversed and fromReversed)
                ):
                    newY = toEndPosition.Y - diff
                else:
                    newY = toStartPosition.Y + diff

            if (toStartPosition.Y == toEndPosition.Y):
                if (
                    (toReversed and not fromReversed)
                    or (not toReversed and fromReversed)
                ):
                    newX = toEndPosition.X - diff
                else:
                    newX = toStartPosition.X + diff
                newY = toStartPosition.Y

            nextOrientation = Point(
                toLimit.orientation.X * -1, toLimit.orientation.Y * -1)

            return Point(newX, newY), nextOrientation
        return None, None

    def getScaledPositions(self, limit):
        limitStartPosition = Point(
            limit.startPosition.X * self.scale, limit.startPosition.Y * self.scale)
        limitEndPosition = Point(
            limit.endPosition.X * self.scale, limit.endPosition.Y * self.scale)
        limitReversed = False

        if (limitStartPosition.X > limitEndPosition.X or limitStartPosition.Y > limitEndPosition.Y):
            limitStartPosition, limitEndPosition = limitEndPosition, limitStartPosition
            limitReversed = True

        if (limit.orientation.X == 0):
            limitEndPosition = Point(
                limitEndPosition.X - 1, limitEndPosition.Y)
        elif (limit.orientation.X == 1):
            limitStartPosition = Point(
                limitStartPosition.X - 1, limitStartPosition.Y)
            limitEndPosition = Point(
                limitEndPosition.X - 1, limitEndPosition.Y)
        if (limit.orientation.Y == 0):
            limitEndPosition = Point(
                limitEndPosition.X, limitEndPosition.Y - 1)
        elif (limit.orientation.Y == 1):
            limitStartPosition = Point(
                limitStartPosition.X, limitStartPosition.Y - 1)
            limitEndPosition = Point(
                limitEndPosition.X, limitEndPosition.Y - 1)

        return limitStartPosition, limitEndPosition, limitReversed
