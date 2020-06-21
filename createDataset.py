import json
import random

dataset = {}

for i in range(1, 500):
    newPoint = {"x": random.gauss(0, 30), "y": random.gauss(0, 30)}
    dataset[i] = newPoint

with open('dataset.json', 'w') as outfile:
    json.dump(dataset, outfile)

print("JSON created")
