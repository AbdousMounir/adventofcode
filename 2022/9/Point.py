class Point(object):
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def __str__(self):
        return "Point(%s,%s)" % (self.X, self.Y)

    def get(self):
        return "Point(%s,%s)" % (self.X, self.Y)

    def moveBy(self, other):
        self.X = self.X + other.X
        self.Y = self.Y + other.Y

    def follow(self, other):
        difX = other.X - self.X
        difY = other.Y - self.Y

        if (difX > 1):
            self.X = self.X + 1
        if (difX < -1):
            self.X = self.X - 1
        if (abs(difX) > 1 and abs(difY) == 1):
            self.Y = self.Y + difY

        if (difY > 1):
            self.Y = self.Y + 1
        if (difY < -1):
            self.Y = self.Y - 1
        if (abs(difY) > 1 and abs(difX) == 1):
            self.X = self.X + difX
