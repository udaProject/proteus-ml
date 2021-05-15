import networkx as net_x
import random
import json
from scipy.spatial import distance as dist
import math
import matplotlib.pyplot as plot
import collections
import numpy as np

from custom_types import buffer, map, vector

# --- Definitions ---

#do some refactoring; create vec class
#overload len() built-in to calculate magnitude
#overload modulus operator to calculate 'a' scaled by mag of 'b' (unit_vec for a % a)
#overload minus operator to calculate vec_diff
#overload plus operator to calculate vec_add
#overload multiplication operator to calculate cos_sim (dot product)

def magnitude(vec):
    if len(vec) == 1:
        return fabs(vec)

    return np.linalg.norm(vec)

def unit_vec(vec):
    magn = magnitude(vec)
    return [comp/magn for comp in vec]

def vec_diff(vec1, vec2):
    diff_vector = []
    if len(vec1) >= len(vec2)
        for label, comp in enumerate(vec1):
            diff_vector[label] = vec2[label] - vec1[label]
    else:
        for label, comp in enumerate(vec2):
            diff_vector[label] = vec2[label] - vec1[label]

    return diff_vector

def vec_add(vec1, vec2):
    add_vector = []
    if len(vec1) >= len(vec2)
        for label, comp in enumerate(vec1):
            add_vector[label] = vec2[label] + vec1[label]
    else:
        for label, comp in enumerate(vec2):
            add_vector[label] = vec2[label] + vec1[label]

    return add_vector

def cos_sim(vec1, vec2):
    return numpy.dot(vec1, vec2) / (magnitude(vec1) * magnitude(vec2))

def signal_count(obj, chart1, chart2, value):
    if value:
        obj.graph.edges[chart1, chart2][(chart1, chart2)] = value
    return obj.graph.edges[chart1, chart2][(chart1, chart2)]

def spring_energy(dist, resist):
    return 0.5*resist*(dist**2)

def calc_resist(obj, hood, chart1, chart2):
    numerator = signal_count(obj, chart1, chart2)
    denominator = fsum( [signal_count(obj, chart1, x) for x in hood] )
    return numerator/denominator

def new_chart(label, ref = None, acc_err = None, heat = 0):
    return (label, {'ref': ref, 'acc_err': acc_err}, 'heat': heat)

def new_link(chart_label1, chart_label2, count_chart1 = 0, count_chart2 = 0, util_chart1 = 0, util_chart2 = 0):
    return (chart_label1, chart_label2, {'chart_label1': {'count': count_chart1, 'util': util_chart1}, 'chart_label2': {'count': count_chart2, 'util': util_chart2}} )

def range_normalize(datum, range):
    left_bound_index = 0
    right_bound_index = 1
    for comp in datum:
        datum[comp] = ( datum[comp] - range[comp][left_bound_index] ) ) / range[comp][right_bound_index])

class data_buffer:
    def __init__(self, data_list, ranges):
        self.index = len(data_list)
        self.ranges = ranges
        self.dim = len(self.ranges)
        self.data = range_normalize(self.data, ranges)
        self.data = random.shuffle(data_list)

    def __iter__(self):
        return self

    def __next__(self):
        next_datum = self.data.pop(self.index)
        self.index += 1
        return next_datum

    def add_datum(datum):
        self.index += 1
        self.data.append( range_normalize(datum, ranges) )

    def merge_buffers(data_buffer):
        self.index += data_buffer
        self.data = random.shuffle( self.data.extend(data_buffer) )
        self.ranges = {**self.ranges, **data_buffer.ranges}
        self.dim = len(self.ranges)

class model_map:
    def __init__(self, ranges):
        self.graph = net_x.Graph()
        vec1, vec2 = defaultdict(list)
        for comp_label, range in enumerate(ranges):
            third = math.fabs(range[1]-range[0])/3
            high = range_normalize(range[1]-third, range)
            low = range_normalize(range[0]+third, range)
            if random.random() >= .5:
                vec1[comp_label].append(low)
                vec2[comp_label].append(high)
            else:
                vec1[comp_label].append(high)
                vec2[comp_label].append(low)

        self.graph.add_nodes_from([
            new_chart(1, vec1),
            new_chart(2, vec2)
        ])

        self.graph.add_edges_from([
            new_link(1, 2)
        ])

# --- Initializations ---

# avoid magic numbers
node_label_index = 0
node_props_index = 1

# get fresh objects
current_buffer = data_buffer()
current_map = model_map()

# Scale factor should always be in range [0,1); '0' corresponds to perfect overfit of the input data (if the algorithm ever converges), '1' corresponds to no node growth ever due to infinite scale.


# calculate a static scale_factor; temporary hack until can be adjusted dynamically
#scale_factor = .85
#scale_factor = .6
scale_factor = .25

ambient_dim = current_buffer.dim
grow_thresh = -ambient_dim*log(1-scale_factor)

# --- Script ---

for index, datum in enumerate(current_buffer):

    print('Debug --- Sample Number: ', index)

    signal = datum

    # calculate differences and magnitudes of nodes to the signal
    diff_vecs_and_magns = {}

    for index, node in enumerate(current_map.graph.nodes):
        diff_vector = vec_diff(node[node_props_index]["ref"], signal)
        magnitude = magnitude(diff_vector)
        label = node[node_label_index]
        diff_vecs_and_magns[label] = {"diff_vector": diff_vector, "magnitude": magnitude}

    # find best matching units
    diff_vec_and_magn_dict = OrderedDict()

    diff_vec_and_magn_dict = sorted(
        diff_vec_and_magn.items(),
        key = lambda node: node['magnitude']
    )

    node_list = list(diff_vec_and_magn_dict.items())
    bmu = node_list[0][0]
    bmu_dist = diff_vec_and_magn_dict[bmu]["magnitude"]
    second_bmu = node_list[1][0]

    print('Debug --- BMU: ', bmu)
    print('Debug --- 2nd BMU: ', second_bmu)

    # if there isn't an edge between 1st & 2nd BMU, create one
    if not current_map.graph.has_edge(bmu, second_bmu):
        current_map.graph.add_edges_from([
            new_link(bmu, second_bmu)
        ])

    # increment the signal counter
    signal_count(current_map, bmu, second_bmu, signal_count(current_map, bmu, second_bmu) + 1)

    # get the neighbors of a node + itself
    bmu_hood = list(current_map.graph.neighbors(bmu))
    second_bmu_hood = list(current_map.graph.neighbors(second_bmu))

    # calculate the error "energy"
    bmu_resist = calc_resist(current_map, bmu_hood, bmu, second_bmu)
    error_energy = spring(bmu_dist, bmu_resist)

    # get the intersection of the two start sets (not guaranteed to be a clique, i.e. a single simplex)
    hood_intersection = [ x for x in bmu_hood.append(bmu) if x in second_bmu_hood.append(second_bmu) ]

    # calculate adaptation for each member of the intersection set
    work_dict = OrderedDict()
    k_dict = OrderedDict()

    for label, node in enumerate(hood_intersection):
        node_hood = list(current_map.graph.neighbors(node))
        if node == bmu:
            k_dict[label] = calc_resist(current_map, node_hood, node, second_bmu)
        else:
            k_dict[label] = calc_resist(current_map, node_hood, node, bmu)

        # hacky temporary approximation
        approx_dim = ( len(hood_intersection)+2 ) / 2

        # calculate deflection of "spring" given electric field of strength determined by error "energy"
        delta_x = (1/k)**(1/approx_dim+1)
        work = spring(delta_x, k)
        work_dict[label] = initial_work

    print('Debug --- K-Array: ', k_dict)

    # hacky temporary approximation of total work done on all nearby nodes by signal since calculating simultaneous action of field on all springs is an expensive multi-body problem; eventually must use a belief propagation algorithm --equivalent to the bethe/kikuchi approximations of the free energy of system
    scaling_factor = 0.5*(error_energy) / fsum(work_dict)
    scaled_work_dict = OrderedDict()
    adaptation_dict = OrderedDict()

    for label, work in enumerate(work_dict):
        scaled_work = work * scaling_factor
        scaled_work_dict[label] = scaled_work
        adaptation = ( scaled_work**0.5 )* 2 / k_dict[label]
        adaptation_dict[label] = adaptation

    print('Debug --- Adaptation Array: ', adaptation_dict)

    residual_error = 0.5*(error_energy)

    # below assignment only holds due to temporary arbitrary choice to split energy half between adaptations and error accumulation
    residual_dict = scaled_work_dict

    grow_nodes = []

    for label, adaptation in enumerate(adaptation_dict):
        node = current_map.graph.nodes[label][node_props_index]
        ref = node['ref']
        diff_vector = diff_vec_and_magn_dict[label]['diff_vector']
        unit_diff_vector = unit_vect(diff_vector)
        adaptation_vector = unit_diff_vector*adaptation
        node['ref'] = vec_add(ref, adaptation_vector)

        # transform residual error into vector in direction of signal
        residual_vector = unit_diff_vector*residual_dict[label]

        # update acc_err
        old_acc_err = node['acc_err']
        node['acc_err'] = vec_add(node['acc_err'], residual_vector)

        # track "destroyed acc_err energy" / "heat"
        for index, old_comp in enumerate(old_acc_err):
            new_comp = node['acc_err'][index]
            delta_heat = 0
            if (old_comp > 0 and new_comp > 0) or (old_comp < 0 and new_comp < 0):
                comp_diff = fabs(new_comp) - fabs(old_comp)
                if comp_diff < 0:
                    delta_heat += magnitude(comp_diff)
            else:
                delta_heat += magnitude(old_comp)

        node['heat'] += delta_heat

        # add new node if accumulated error exceeds growth threshold
        if node['acc_err'] >= grow_thresh:
            grow_nodes[label] = node

    for label, grow_node in enumerate(grow_nodes):
        grow_node_ref = grow_node[node_props_index]['ref']
        grow_node_err = grow_node[node_props_index]['acc_err']
        grow_node_hood = list(current_map.graph.neighbors(grow_node))

        proj_err = {}

        for label, node in enumerate(grow_node_hood):
            hood_node_ref = node[node_props_index]['ref']

            # find projections of acc_err onto vector between grow_node + neighbors and vice versa, i.e calculate acc_err quantized to graph edges
            # find largest sum of projections for any pair == largest error subgradient
            left_edge_vec = vec_diff(grow_node_ref, hood_node_ref)
            left_project = cos_sim(grow_node_err, left_edge_vec)
            left_proj_acc_err = unit_vec(left_edge_vec)*left_project

            right_edge_vec = vec_diff(hood_node_ref, grow_node_ref)
            right_project = cos_sim(grow_node_err, right_edge_vec)
            right_proj_acc_err = unit_vec(right_edge_vec)*left_project

            pair_proj_sum = left_proj_acc_err + right_proj_acc_err
            proj_err[label] = {
                'left': left_proj_acc_err,
                'right': right_proj_acc_err,
                'sum': pair_proj_sum
            }

        proj_err_dict = OrderedDict()

        proj_err_dict = sorted(
            proj_err.items(),
            key=lambda entry: entry[1]['sum']
        )

        pair_proj_list = list(proj_err_pair_sum_dict.items())

        top_sum_label = pair_proj_list[0][0]
        top_left_proj = pair_proj_list[0][1]['left']
        top_right_proj = pair_proj_list[0][1]['right']

        # need to keep track of each projection along with sum in order to calculate how much error can be transfered to new node as utility/binding energy



# --- Execute test ---

# Load test dataset
with open('dataset.json') as json_file:
    dataset = json.load(json_file)
