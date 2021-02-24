

# Import data set. Assume all data points are comprised of a common domain of vector components.

# Initialize with 2 nodes in graph data structure; they should be connected by an edge. Each node has an associated reference vector whose components match the domain of the data points. Each node has a list of directed edges to other nodes. The edges in each node's list contain a reference to the node pointed to, a real-valued signal counter, and a real-valued 'utility' variable. Each node has an accumulated error vector rooted at the head of the reference vector of the node.

"""
Example:

node1: {
  ref:,
  acc_err:,
  edges: {
    edge1: {
      link: node2,
      count:,
      util:
    },
    edge2: {
    ...
    ...
  }
},
node2: {
...
...
"""

# Sample data point of data set. Compute distance of point to all existing nodes in graph.

# Select the 2 nodes that have the minimum distance to the sampled data point.

# Consider the closest node the 1st BMU (the best matching unit) and the second closed the 2nd BMU.

# If there is no edge between the 1st and 2nd BMU, create one; this entails creating an entry in both nodes since the edges are directed. Then set signal counter of the BMU toward the 2nd BMU to '1'; otherwise, increment signal counter of the BMU directed toward the 2nd BMU by '1'.

# Identify the topological neighbors of the 1st BMU and the 2nd BMU. Find the intersection of the two sets. !!!Is not necessary a clique; must run algo to find subset of these vertices that define a clique!!! This defines a simplex containing the signal.

# Compute difference between the signal vector (sampled data point) and vertices of the simplex.

# The difference between the BMU and the signal should be the smallest (by definition of the BMU). Use this distance to calculate the amount of "work" that would be required to move the BMU to the signal.

# For now, define 'k' as the sum of all the counters across all of the nodes edges over the value of the counter from the 1st BMU to 2nd BMU. That is, edge_counter(1stBMU_to_2ndBMU) /divide /sum_over_all_edges( edge_counters )

# The "work" (error energy) done is k*(1/t)*(magnitude_of_difference)^2 where t = -D*log(1-SF)

# The idea is to treat the "work" that would have been required to move the BMU to the signal as the current error of the model (in terms of the energy that would be required to remove the error completely by moving the node to the signal). We want to remove some of the error by computing changes to the reference vectors of nodes in the simplex containing the signal.

# Changes to reference vectors of nodes in the simplex containing the signal labeled as shifts.

# Add shifts for each node to their respective "avg_err" props.

# Magnitude of "destroyed" avg_err caused by previous step is added to node "acc_heat"

# If avg_err/sqrt(total_count) < \phi * sqrt(t), where 't' is scale parameter and \phi = t_exp/temp_avg and t_exp = temp * (.7)^2 and temp = acc_heat/(total_count-1) and temp_avg = sum(temp_n)/total_nodes

# Compute error energies w/ resp. to signal for all nodes in simplex. Difference between shift and error energy is residual error energy.

# Residual error energy of 1stBMU (node0) is actually a total error (since error is defined by in reference to this node)

# (node1 res. error energy) - (node0 total error energy)
# ---> edge 1,0 utility (binding energy)

# (node2 res. error energy) - (node1 res. error energy) - (node0 total error energy)
# ---> edge 2,0 utility (binding energy)

# Continue for all nodes

# Should in general be some total error energy left (because of inverse quadratic dependence on distance and assumption about ordering (node3 farther away than node2 farther away than node1 from node0, etc...) ).

# Add final remaining residual to "acc_res" prop

# For any node in simplex, if mag(acc_res) + (avg_err * acc_res) >= GT then trigger node growth in direction of acc_res.

# Place new node avg( mag(edge links) ) distance in direction of acc_res?
