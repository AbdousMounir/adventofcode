from input import input1, input2


case1 = input1.split('\n')
case2 = input2.split('\n')


def lookAndCount(x, y, forest, interval, ratioX, ratioY):
    treeInView = 0
    for index in range(interval):
        treeInView += 1
        if (int(forest[y + (ratioY * index) + ratioY][x + (ratioX * index) + ratioX]) >= int(forest[y][x])):
            return False, treeInView
    return True, treeInView


def run(case):
    count = 0
    treeScores = []
    for y in range(len(case)):
        for x in range(len(case[y])):
            lookUp, countUp = lookAndCount(x, y, case, y, 0, -1)
            lookDown, countDown = lookAndCount(
                x, y, case, len(case) - y - 1, 0, 1)
            lookRight, counRight = lookAndCount(
                x, y, case, len(case[y]) - x - 1, 1, 0)
            lookLeft, countLeft = lookAndCount(x, y, case, x, -1, 0)

            if (
                lookUp |
                lookDown |
                lookRight |
                lookLeft
            ):
                count += 1

            treeScores.append(countUp * countDown * counRight * countLeft)
    return count, max(treeScores)


print(run(case2))
