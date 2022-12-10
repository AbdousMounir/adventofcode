class Console(object):
    def __init__(self, maxSize, maxSpace):
        self.drive = {}
        self.currentPath = []
        self.maxSize = maxSize
        self.maxSpace = maxSpace

    def __str__(self):
        return "=> %s/ ~" % ("/".join(self.currentPath))

    def openFolder(self):
        currentFolder = self.drive
        for path in self.currentPath:
            currentFolder = currentFolder[path]
        return currentFolder

    def runLine(self, line):
        if (line[:2] == "$ "):
            if (line[2:5] == "cd "):
                if (line[5] == "/"):
                    self.currentPath = []
                elif (line[5:7] == ".."):
                    del self.currentPath[-1]
                else:
                    self.currentPath.append(line[5:])
        else:
            info, name = line.split()
            if (info == 'dir'):
                self.openFolder()[name] = {}
            else:
                self.openFolder()[name] = int(info)

    def getFolderSizeFlatten(self, folder):
        totalSize = 0
        for value in folder.values():
            if (type(value) == int):
                totalSize += value
            elif (type(value) == dict):
                totalSize += self.getFolderSizeFlatten(value)
        self.folderSizeFlatten.append(totalSize)
        return totalSize

    def getSpaceToSave(self):
        self.folderSizeFlatten = []
        self.getFolderSizeFlatten(self.drive)
        return sum(filter(lambda x: (x < self.maxSize), self.folderSizeFlatten))

    def getFolderSizeToDelete(self):
        self.folderSizeFlatten = []
        self.getFolderSizeFlatten(self.drive)
        minimumSpaceNeeded = max(self.folderSizeFlatten) - self.maxSpace
        return min(filter(lambda x: (x > minimumSpaceNeeded), self.folderSizeFlatten))
