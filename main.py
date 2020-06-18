import networkx as nx
import random
import json
from scipy.spatial import distance
import math
import matplotlib.pyplot as plt
from collections import Counter

# = counter of edge a-b / sum of counters of all edges for node a


def spring(eucDist, resistance):
    return 0.5*resistance * eucDist * eucDist


def euclideanDistance(a, b):
    return distance.euclidean(list(a.values()), list(b.values()))


globalCounter = Counter()


# Load the dataset
with open('dataset.json') as json_file:
    dataset = json.load(json_file)


# Init the graph
G = nx.DiGraph()


# init 2 starting points
startPoint1 = {"x": random.randint(0, 100), "y": random.randint(0, 100)}
while True:
    startPoint2 = {"x": random.randint(0, 100), "y": random.randint(0, 100)}
    if startPoint1 != startPoint2:
        break


G.add_node(1, position=startPoint1)
G.add_node(2, position=startPoint2)

G.add_edge(1, 2)


G.add_edge(2, 1)

# sample data points

for sampleDataPoint in dataset:
    samplePosition = dataset[sampleDataPoint]

    # check 2 closest nodes

    nodesList = list(G.nodes(data=True))

    nodesList.sort(key=lambda x: euclideanDistance(
        x[1]["position"], samplePosition))

    differenceVectorsAndMagnitudeArray = [
        {"vector": (samplePosition["x"] - nn[1]["position"]["x"], samplePosition["y"] - nn[1]["position"]["y"]), "magnitude": euclideanDistance(samplePosition, nn[1]["position"])
         } for nn in nodesList
    ]

    differenceVectorsAndMagnitudeDict = {}
    for index, content in enumerate(nodesList):
        differenceVectorsAndMagnitudeDict[content[0]
                                          ] = differenceVectorsAndMagnitudeArray[index]

    bestNode = nodesList[0][0]
    bestNodeDistance = differenceVectorsAndMagnitudeDict[nodesList[0]
                                                         [0]]["magnitude"]
    secondBestNode = nodesList[1][0]
    secondBestNodeDistance = differenceVectorsAndMagnitudeDict[nodesList[1]
                                                               [0]]["magnitude"]
    print("Best node ", bestNode)
    # if there isnt an edge, lets create one
    if not G.has_edge(bestNode, secondBestNode):
        G.add_edge(bestNode, secondBestNode)
        G.add_edge(secondBestNode, bestNode)

    # increment the counter
    globalCounter[(bestNode, secondBestNode)] += 1
    # get the neighbors + itself
    bestNodeNeighbors = list(G.neighbors(bestNode))+[bestNode]
    secondBestNodeNeighbors = list(
        G.neighbors(secondBestNode))+[secondBestNode]

    # get the intersection AKA SIMPLEX
    neighborsIntersection = [
        x for x in bestNodeNeighbors if x in secondBestNodeNeighbors]

    counterSumOfDiEdgesFromBMU = sum(
        [globalCounter[(bestNode, x)] for x in list(G.neighbors(bestNode))])

    errorWork = spring(bestNodeDistance, globalCounter[(
        bestNode, secondBestNode)] / counterSumOfDiEdgesFromBMU)

    # calculate the new position for each neighbour of BMU and 2nd BMU

    initialWorkArray = []
    kArray = []
    for neighb in neighborsIntersection:

        if neighb == bestNode:
            k_numerator = globalCounter[(neighb, secondBestNode)]
        else:
            k_numerator = globalCounter[(neighb, bestNode)]

        k_denominator = sum([globalCounter[(neighb, x)]
                             for x in list(G.neighbors(neighb))])

        k = k_numerator / k_denominator
        kArray.append(k)

        if len(list(G.neighbors(neighb))) > 1:
            dimensionality = 2
        else:
            dimensionality = 1

        delta_x = (1/k)**(1/dimensionality+1)

        initial_work = spring(delta_x, k)
        initialWorkArray.append(initial_work)
    scalingFactor = 0.5*(errorWork) / sum(initialWorkArray)
    scaledWorkArray = [x * scalingFactor for x in initialWorkArray]
    backwardsArray = []
    for scaledIndex in range(len(scaledWorkArray)):
        x = scaledWorkArray[scaledIndex]
        x2 = x**0.5 * 2 / kArray[scaledIndex]
        backwardsArray.append(x2)

    print("errorWork ", errorWork)

    break
