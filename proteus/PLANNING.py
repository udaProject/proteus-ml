
#############
# This file is for brainstorming/scaffolding purposes only
#############


# Dependencies
import math
import numpy
import scipy
import scikit
import networkx

# Import data parser
import data_parser as datpar
# Import unsupervised NN primitive
import growing_neural_gas as grwgas
# Import fuzzy logic handler
import fuzzy_logic as fuzlog

#########################
###### Build model ######
#########################


# def manifold.grow(data_set):
    # Create manifold object representing a new model using a provided data set.

    # Initialize top level chart

    # Sample data vector and feed to chart. If BMU is contained in scale
    # convergent cluster, complete run in top level chart and then shunt data
    # to sub-chart for further processing.

        # Identify first and second best matching unit (node); reference vectors
        # closest to data point in terms of Euclidean distance (for now).

        # If edge between 1st and 2nd BMU doesn't exist, create it. Increment
        # counter on directed edge from 1st BMU to 2nd BMU.

        # Compute adaptation for all nodes that form vertices of containing
        # simplicial cell. Magnitude of adaptations are added to respective
        # edge to BMU as utility.

        # The residual fraction of distance between BMU and data point is added
        # to BMU's accumulated error vector.

        # If accumulated error vector crosses growth threshold, initiate growth
        # procedure.

    # Check relative edge counters and node total utility per counter. If either
    # meets conditions, initiate edge deletion/node deletion procedure,
    # respectively.

    # Check if node appears very close to local uniform density. If passes test,
    # set as cluster candidate. Greedily merge candidates when adjacent. Better way of seeding cluster candidates???

    # Treat cluster candidate as fixed region and assign other non-candidate
    # nodes to maximize objective function (maximize correlation/similarity of a
    # cluster node's neighborhood with rest of cluster candidate set).

    # Estimate cluster support by iterative PCA to obtain principal components
    # and estimate volume as ellipsoid.

    # Iteratively estimate the change in support (volume) conditioned on
    # change in resolution factor (i.e. maximal Gaussian response in
    # scale-space)??? Better way to compute change in support conditional on scale factor???

    # If cluster candidate's change in support conditioned on change in
    # resolution factor indicates to within some confidence a negative 2nd
    # derivative and a zero 1st derivative, then consider it "scale convergent".

        # Finalize calculation of PCA. Repair data buffer for cluster, then
        # project all buffered data into subspace defined by new basis vectors.

        # Initialize new chart in sub-space and stream feed all buffered data.

    # Adjust scale factor, if needed, for each cluster candidate.

    # Terminate when all clusters/nodes in a cluster have too few points for
    # statistically valid measurement and/or minimum distance between two points
    # in a cluster is larger than the scale variance sampling threshold.


#####################
###### Utility ######
#####################


# def manifold.stream_add(new_data_vector):
    # Add single new data vector to existing model in manifold object.


# def manifold.batch_add(new_data_batch):
    # Add new batch of data vectors to existing model in manifold object. Not
    # functionally different from stream_add, merely a convenience. Will
    # automate feeding in data vectors in one at a time from batch.


# manifold.charts
    # The trie of charts (multi-scale soft clusters) in the model.


# manifold.chart_idents[some_chart_label]
    # Dictionary.
    # Returns a two-element array containing the identifier for a
    # given chart label and an identifier the corresponding data vector
    # bundle.
    #
    # NOTE: Always save and pass references to the chart label, *never* the
    # chart identifier directly since it can change unpredictably at run-time.
    # However, each identifier is augmented with a unique ordering token that
    # can be used to provide static references to a chart independently of the
    # label (which can also be changed at run-time). Retrieving a chart using
    # the unique ordering token takes O(logN) time (where N is the number of
    # charts) instead of a regular O(1) hash table lookup.


# some_chart_ident
    # Two-element array containing dynamic trie string (for efficient
    # navigation) and a unique ordering token.


# some_ordering_token
    # A three-element array containing a hash value and two references to other
    # ordering tokens based on a DeBruijn graph scheme. (can be built dynamically)


# manifold.data_bundles[some_bundle_identifier]
    # Returns a two-element array containing a dictionary and a bloom filter.
    # Each dictionary corresponds to the data vectors "held in" a particular
    # chart. The bloom filter is used during reverse look-up.


# some_data_bundle
    # A dictionary.
    # The entries map data vector labels to a two-element array of the data
    # vector hash and corresponding chart ordering token.


# manifold.data_vectors[some_data_vector_hash]
    # Returns a data vector.
    # Dictionary containing all data vectors fed into the model.


# some_data_vector
    # A tuple of data values. Augmented with a type value to keep track of
    # which vectors are original data and which are virtual data.


# def manifold.chart_path(some_chart_label):
    # Return the labels of all charts on the trie path to the given chart.


# def manifold.chart_label(some_chart_path):
    # Return the label for a given chart path.


# def manifold.walk(some_chart_label):
    # Return the chart object corresponding to the given label.


# some_chart.prototypes
    # Return the prototypes in a chart (virtual exemplars [node weight vectors
    # MaxEnt approximating the PDF of the distribution induced by the modeled
    # data set]).


# some_chart.examplars()
    # Return exemplars (real data vectors closest to prototypes [node weight
    # vectors]).


# some_chart.chart_centroid
    # Return a virtual prototype corresponding to the centroid (the first
    # moment) of the given chart.


# some_chart.chart_prototype
    # Return the prototype most representative (closest to the centroid) of the
    # given chart.


# some_chart.chart_exemplar
    # Return the exemplar most representative (closest to the centroid) of the
    # given chart.


#################################
###### Analytic Operations ######
#################################


# def manifold.prim_membership(some_vector_label):
    # Returns an array of two-element tuples composed of chart labels from
    # charts encountered along the path and the corresponding membership value
    # in those charts for the specified data vector. (the left-to-right order of the tuples in the array corresponds to a total inclusion ordering over the referenced charts)


# def manifold.classify(subset_of_data_vectors):
    # Returns fuzzy predicates corresponding to one or more decision boundaries
    # on the modeled manifold.
    # The input is a list of the data vector labels corresponding to data vectors
    # that should be used to generate the fuzzy predicates.


# def manifold.generate(some_fuzzy_predicates, quantity):
    # Generate virtual data vectors stochastically sampled from the new manifold
    # defined by the given tuple of fuzzy predicates.


# def manifold.query(some_fuzzy_predicates, return_limit)
    # Return a subset, whose max size is restricted to the return_limit, of the
    # fuzzy set defined by the given predicates.


#######################
# NOTE: manifold.grow (generating a model from data points) is the complement of
# manifold.generate (generating data points from a model). Similarly,
# manifold.classify (finding constraints that match some data points) is the
# complement of manifold.query (finding data points that match some constraints).
#######################


# def manifold.semantics(some_fuzzy_predicates):
    # Enters an interactive sequence where exemplars/prototypes of the described
    # set (primitive or composite) are returned to the user in small batches.
    # The user controls how many times this occurs and terminates the
    # interactive sequence by choosing a new binding (label) for the given set
    # based on their perception of the similarities of the set members.
    #
    # NOTE: This can be used to teach the model arbitrary "language", and is vital
    # for enabling interpretability of the model.

# manifold.compset_idents[some_composite_set_label]
    # A dictionary.
    # Returns a list of fuzzy predicates associated with the given label (bound
    # through a manifold.semantics call).

# def manifold.comp_membership(manifold.prim_membership(some_vector_label)):
    # Takes the primitive membership values of a data vector and returns all
    # composite membership values calculated from the fuzzy predicates stored in
    # compset_idents.
