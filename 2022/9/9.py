from Point import Point
from input import input1, input2, input3

mouvement = {
    "U" : Point(0,1),
    "R" : Point(1,0),
    "D" : Point(0,-1),
    "L" : Point(-1,0),
}

rope = []
for i in range(10):
    rope.append(Point(0,0))

case1 = list(map(lambda x: x.split(), input1.split('\n')))
case2 = list(map(lambda x: x.split(), input2.split('\n')))
case3 = list(map(lambda x: x.split(), input3.split('\n')))

def run(case):
    positionHistory = [rope[-1].get()]
    for move in case:
        for _ in range(int(move[1])):
            rope[0].moveBy(mouvement[move[0]])
            for knotIndex in range(len(rope) - 1):
                rope[knotIndex + 1].follow(rope[knotIndex])
            if (rope[-1].get() not in positionHistory):
                positionHistory.append(rope[-1].get())
    return positionHistory

case2History = run(case2)
print(len(case2History))
