import math
from collections import Counter


class Point:
    def __init__(self, label, neighbours, x, y, z=0):
        self.label = label
        self.x = x
        self.y = y
        self.z = z
        self.neighbors = neighbours
        self.errorVector = [0, 0, 0]

        # if this point has 5 victories over point2, {"point2" : 5}
        self.winsOverOtherPoint = Counter()

        # if this point has 5 losses over point2, {"point2" : 5}
        self.lossesOverOtherPoint = Counter()

    def euclidianDistanceToNewPoint(self, x, y, z):
        print("FINISH THIS")
        return 0

    def updateErrorVector(self, x, y, z):
        # update the error vector
        print("FINISH THIS")
        if error > self.threshold:
            self.splitPoint()


class Proteus:
    def __init__(self):
        point1 = Point("point1", "point2", 0, 0)  # x, y
        point2 = Point("point2", "point1", 50, 50)
        self.points = [point1, point2]
        self.threshold = 30  # ??

    def importFromJson(self, j):
        pass

    def exportToJson(self):
        pass

    def feedDataPoint(self, x, y, z=0):
        bestResult = math.inf
        secondBestResult = math.inf
        bestPointIndex = 0
        secondBestPointIndex = 0

        for i, p in enumerate(self.points):
            dist = p.euclidianDistanceToNewPoint(x, y, z)
            if dist < bestResult:
                bestResult = dist
                bestPointIndex = i
            elif dist < secondBestResult:
                secondBestResult = dist
                secondBestPointIndex = i

        # update the wins over and losses over counters
        self.points[bestPointIndex].winsOverOtherPoint[self.points[secondBestPointIndex].label] += 1
        self.points[secondBestPointIndex].lossesOverOtherPoint[self.points[bestPointIndex].label] += 1

        # update error vector
        self.points[bestPointIndex].updateErrorVector(x, y, z)
