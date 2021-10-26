## Phase 1
- [ ] Figure out some sticking points concerning how 'resources' are defined and used to inform the adaptation of nodes.
- [ ] Figure out more concretely how convergence of network during training will be measured and tracked.
- [ ] Have custom GNG variant run smoothly for any fixed scale factor to convergence on a reasonably complex test data set, with the expected properties: local topological links between nodes are good estimation of local intrinsic dimensionality of data, the Voronoi regions of all nodes form an approximately equiprobable quantization of the PDF of the input distribution, the learning procedure converges relatively quickly.
- [ ] Ideally, rules used for node insertion, deletion, and adaptation are well-founded. If possible, have the mechanisms used to keep track of error and other "resources" conform to a general notion of 'conservation of energy'.
- [ ] Have an online clustering algorithm run on the nodes of the converged GNG network and successfully identify and separate simple unimodal clusters. Most likely option is some form of belief/affinity propagation and/or a max-flow/min-cut algorithm or some fusion of both?
- [ ] Be able to run custom GNG variant on same data set for two or more different (but close together) fixed scale factors, generate respective maps, and perform online clustering on maps, then evaluate and compare matching clusters (clusters in identical locations in all the maps) using some sort of operator that changes continuously in scale-space. Options are to explicitly measure statistical similarity of a cluster to a true Gaussian of similar width as cluster, or to implicitly measure by looking at growth of the cluster's support. Then be able to identify inflection points (second derivatives) in behavior of operator on clusters through scale-space. In fewer words, objective is to identify local maxima of Gaussian response of distribution in scale-space.
- [ ] Be able to grow maps, perform clustering, and measure Gaussian response while continuously changing the scale-factor at run-time. Changes to scale-factor could be done using an exponential schedule, increasing until inflection point is overshot then decreasing as it bounces on either side and converges to correct value of scale-factor.
- [ ] Refactor, formalize data structures, improve overall quality of code.
- [ ] Figure out how to take topological net of a discovered cluster in a map and compute an affine local coordinate system from it; in other words, a cluster of nodes in a map may represent a submanifold that has intrinsic curvature that cannot be approximated with affine transformations and needs to be processed by a non-linear transformation before an affine coordinate system can be defined on it. Some sort of simple deep neural net of one or two layers? We would know the input dimension (the current dimension of data points for that map) and the output dimension (the local dimensionality of the cluster estimated by the topological links) but necessarily exactly not how complex the needed transformation will be and thus how wide the NN would need to be. Perhaps some sort of power series analysis to estimate degree of required polynomial?
- [ ] Take output of above step and instead of using input dimensionality for all levels of maps, cast data points into the 'unwrapped' principle components (local coordinates) of clusters they belong to at every level before recursively computing the next lower level, etc... This allows distance computations at every level to be less expensive than when always using the ambient input data dimensions.
- [ ] Use Euclidean representations of clusters to compute the fuzzy logical membership function value for data points for all scale-space clusters they belong to. When a full hierarchy is learned for a data set, be able to transform all data points in data set from vectors in input dimensions to vectors of cluster membership values.
- [ ] Refactor, formalize data structures, improve overall quality of code.
- [ ] Publish paper?

## Phase 2
- [ ] Explore use of similarity search structures to reduce number of distance calculations needed when finding best matching node in a map for an input datum during training.
- [ ] Explore relationship to wavelet analysis techniques and use of sampling at the Nyström limit to reduce how often nodes/maps need to process new data points if data points are being streamed in continuously.
- [ ] Explore use of RKHS and other kernel methods to improve efficiency or accuracy of node adaptions.
- [ ] Explore more explicit use of Bregman divergences as framework for adaptation mechanisms.
- [ ] Explore use of similarity hashing and other metric reduction techniques to further speed up distance calculations.
- [ ] In general, explore various methods for optimizing various parts of Proteus up to this point.
- [ ] Publish paper?

## Phase 3
- [ ] Use "t-SNE" or equivalent technique to allow any map to be embedded into a 2D or 3D approximation for visualization purposes. Ideally, a nice GUI for navigating the tree hierarchy of maps/scale-space clusters (atlas) and clicking on any one to calculate/view an embedding for that "natural feature".
- [ ] Decide on which definitions/framework will be used for fuzzy logical operators.
- [ ] Implement a sampling method to generate fake/interpolated data from any atlas. Maybe some sort of graph random walk technique mixed with mesh interpolation?
- [ ] Extend sampling method from baseline predicates (i.e. some clusters are contained in others and sampling an atlas requires taking this into account) to arbitrary fuzzy zeroth-order logical predicates over the atoms (fuzzy membership functions for each cluster). Probably will require use of survey propagation techniques?
- [ ] Ensure solid framework is established for understanding metric behavior of fuzzy logical predicates.
- [ ] Ensure solid framework is established for understanding RKHS behavior of treating the output of arbitrary predicates as new atoms that can be used to form higher-order predicates.
- [ ] Publish paper?

## Phase 4
- [ ] Design procedure for semi-supervised labeling of scale-space clusters; procedure would include generating multiple virtual data points from a cluster and asking for user to input a label in natural language that describes the conceptual overarching commonality between the examples.
- [ ] Design procedure for taking data points that have been manually classified and generating a fuzzy logical predicate for each class both 1) serves as a complete description of that class which can be used to identify new examples of the class and 2) can be used to generate virtual data points of the class.
- [ ] Publish paper?

## Phase 5
- [ ] Design procedure for identifying REAL data from the original data set that match an arbitrary zeroth-order fuzzy predicate query. Explore possibility of extending to first-order predicates.
- [ ] Design a querying language that formalizes a fuzzy relational algebra for the fuzzy predicates. Enable use of this more formal DSL in user interactions.
- [ ] Publish paper?

## Phase 6
- [ ] Explore how to extend system to non-stationary distributions.
- [ ] Explore applications to time-series prediction and optimal, adaptive compression of data streams.
- [ ] Explore application of system to the distributed setting, both for concurrent/parallel speedups, but also to the question of learning connectivity graphs for completely self-organizing P2P databases.
- [ ] Publish paper?
