

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

# Identify the topological neighbors of the 1st BMU and the 2nd BMU. Find the intersection of the two sets. This defines a simplex containing the signal.

# Compute difference between the signal vector (sampled data point) and vertices of the simplex.

# The difference between the BMU and the signal should be the smallest (by definition of the BMU). Use this distance to calculate the amount of "work" that would be required to move the BMU to the signal.

For now, define 'k' as the sum of all the counters across all of the nodes edges over the value of the counter from the 1st BMU to 2nd BMU. That is, edge_counter(1stBMU_to_2ndBMU) /divide /sum_over_all_edges( edge_counters )

The "work" done is (1/2)*k*(magnitude_of_difference)^2

# The idea is to treat the "work" that would have been required to move the BMU to the signal as the current error of the model (in terms of the energy that would be required to remove the error completely by moving the node to the signal). We want to remove some of the error by computing changes to the reference vectors of nodes in the simplex containing the signal. We'll do this by imagining that the signal is emitting an electric field that is attracting all the nodes in the simplex. The force of the attraction will be an inverse power law (where the exponent depends on a local approximation of the dimensionality). The local approximation of the dimensionality is simply the number of edges the BMU has minus 1.
