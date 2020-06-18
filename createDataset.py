import json
import random


dataset = {}

for i in range(1, 200):
    newPoint = {"x": random.randint(0, 100), "y": random.randint(0, 100)}
    if not(newPoint in dataset.values()):
        dataset[i] = newPoint
    else:
        print("repeated")


with open('dataset.json', 'w') as outfile:
    json.dump(dataset, outfile)


print("JSON CREATED")
