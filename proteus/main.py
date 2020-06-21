import networkx as net_x
import random
import json
from scipy.spatial import distance as dist
import math
import matplotlib.pyplot as plot
import collections

# --- Definitions ---

def signal_count(obj, node1, node2, value):
    if value:
        obj.graph.edges[node1, node2][(node1, node2)] = value
    return obj.graph.edges[node1, node2][(node1, node2)]

def spring_energy(dist, resist):
    return 0.5*resist*(dist**2)

def L2_dist(a, b):
    return dist.euclidean(list(a.values()), list(b.values()))

def calc_resist(obj, hood, node1, node2):
    numerator = signal_count(obj, node1, node2)
    denominator = sum( [signal_count(obj, node1, x) for x in hood] )
    return numerator/denominator

class data_buffer:
    def __init__(self, data):
        self.data = random.shuffle(data)
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        next_datum = self.data.pop(self.index)
        self.index += 1
        return next_datum

    def add_datum(datum):
        self.index += 1
        self.data.append(datum)

    def merge_buffers(data_buffer):
        self.index += data_buffer.
        self.data.extend(data_buffer)

class model_map:
    def __init__(self, ranges):
        self.graph = net_x.Graph()
        temp = defaultdict(list)
        for range in ranges:
            third = math.fabs(range[1]-range[0])/3
            if random.random() >= .5:
                temp[0].append([range[0]+third)
                temp[1].append(range[1]-third])
            else:
                temp[1].append([range[0]+third)
                temp[0].append(range[1]-third])
        self.graph.add_node(1, chart_vector=temp[0])
        self.graph.add_node(2, chart_vector=temp[1])

        # model bidirectional weighted graph as undirected graph with attributes
        self.graph.add_edge(1, 2)
        signal_count(self, 1, 2, 0)
        signal_count(self, 2, 1, 0)

# --- Initializations ---

current_buffer = data_buffer()
current_map = model_map()

# avoid magic numbers
node_label_index = 0
node_props_index = 1

# --- Script ---

for datum in current_buffer:

    signal = datum
    node_list = current_map.graph.nodes

    # check for best-matching units
    node_list.sort(key=lambda node: L2_dist(
        node[node_props_index]["chart_vector"], signal))

    # calculate differences and magnitudes
    diff_vec_and_magn_array = []

    for index, node in enumerate(node_list):
        diff_vector = []
        for comp in signal:
            diff_vector[comp] = signal[comp] - node[node_props_index]["chart_vector"][comp]

        magnitude = L2_dist(signal, node[node_props_index]["chart_vector"])

        diff_vec_and_magn_array[index] = {"diff_vector": diff_vector, "magnitude": magnitude}

    # match to correct node label
    diff_vec_and_magn_dict = OrderedDict()

    for index, node in enumerate(node_list):
        node_label = node[node_label_index]
        diff_vec_and_magn_dict[node_label] = diff_vec_and_magn_array[index]

    bmu = node_list[node_label_index]
    bmu_dist = diff_vec_and_magn_dict[bmu]["magnitude"]
    second_bmu = node_list[node_label_index]
    second_bmu_dist = diff_vec_and_magn_dict[second_bmu]["magnitude"]

    print('Debug --- BMU: ', bmu)

    # if there isn't an edge  between 1st & 2nd BMU, create one
    if not current_map.graph.has_edge(bmu, second_bmu):
        current_map.graph.add_edge(bmu, second_bmu)
        signal_count(current_map, bmu, second_bmu, 0)
        signal_count(current_map, second_bmu, bmu, 0)

    # increment the signal counter
    signal_count(current_map, bmu, second_bmu, signal_count(current_map, bmu, second_bmu) + 1)

    # get the neighbors of a node + itself
    bmu_hood = list(current_map.graph.neighbors(bmu))
    second_bmu_hood = list(current_map.graph.neighbors(second_bmu))

    # calculate the error "energy"
    bmu_resist = calc_resist(current_map, bmu_hood, bmu, second_bmu)
    error_energy = spring(bmu_dist, bmu_resist)

    # get the intersection of the two sets (a rhomboidal simplicial complex)
    hood_intersection = [ x for x in bmu_hood.append(bmu) if x in second_bmu_hood.append(second_bmu) ]

    # calculate adaptation for each member of the intersection set
    initial_work_array = []
    k_array = []

    for node in hood_intersection:
        node_hood = list(current_map.graph.neighbors(node))
        if node == bmu:
            k_array.append( calc_resist(current_map, node_hood, node, second_bmu) )
        else:
            k_array.append( calc_resist(current_map, node_hood, node, bmu) )

        approx_dim = ( len(hood_intersection)+2 ) / 2

        delta_x = (1/k)**(1/approx_dim+1)

        work = spring(delta_x, k)
        work_array.append(initial_work)

    scaling_factor = 0.5*(error_energy) / sum(work_array)
    adaptation_array = []

    print('Debug --- Scaling Factor: ', scaling_factor)

    for index, work in enumerate(work_array):
        scaled_work = work * scaling_factor
        work_array[index] = scaled_work
        adaptation = ( scaled_work**0.5 )* 2 / k_array[index]
        adaptation_array.append(adaptation)

    residual_error = 0.5*(error_energy)
    # below equality only holds due to choice to split energy half between adaptations and error accumulation
    residual_array = work_array

    for label in hood_intersection:
        chart_vector = current_map.graph.nodes[label]["chart_vector"]
        diff_vector = diff_vec_and_magn_dict[label]["diff_vector"]
        for comp in chart_vector:
            chart_vector[comp] = chart_vector[comp] + diff_vector[comp]

        # write code to accumulate error; requires adding "acc_err" var to nodes; then need to add code for node growth.

# --- Execute test ---

# Load test dataset
with open('dataset.json') as json_file:
    dataset = json.load(json_file)
