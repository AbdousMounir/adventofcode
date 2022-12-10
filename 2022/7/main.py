from input import input1, input2
from Console import Console


case1 = input1.split('\n')
case2 = input2.split('\n')


def run(case):
    console = Console(100000, 70000000 - 30000000)
    for line in case:
        console.runLine(line)
    return console.getSpaceToSave(), console.getFolderSizeToDelete()


print(run(case2))
