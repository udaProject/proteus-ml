# Papers

## GDrive
https://drive.google.com/drive/folders/10720wqbROytzDo8puYq0HV_XDpxMc-G9?usp=sharing

## Main

### main.1 - Growing Networks
- "A Resource-Allocating Network for Function Interpolation"; original paper proposing optimization using 'resources' cited in Fritzk's "Growing Cell Structures" and subsequently the following three papers.

- "Growing Cell Structures"; Predecessor work to "Growing Neural Gas"; some details missing in GNG paper can be found here.

- "Multiple Growing Cell Structures"; example of calculating receptive area of charts as Gaussian activation with standard deviation set by mean distance to topological neighbors; lists multiple types of error measures that can be used as the error 'resource' (squared error, mean squared error, logarithmic error, Bernoulli error); example of redistributing error 'resource' between neighboring nodes as part of network adaptation.

- "Hierarchical Growing Cell Structures"; example of a hierarchical growing network.

-  "A self-organising network that grows when required"; proposes rigorous measures of performance for topology preserving networks.

- "A Neural-Gas Network Learns Topologies"; original paper proposing technique for triangulation/discovery of local intrinsic dimensionality of point cloud later used by Fritzk in "Growing Neural Gas" below.

- "A Growing Neural Gas Network Learns Topologies"; baseline reference for a growing neural network.

- "Dynamic Self-Organizing Maps with Controlled Growth for Knowledge Discovery"; proposes definition of 'scale factor'; demonstrates a working scheme for a hierarchy of growing networks at different scales, but uses less sophisticated techniques.

- "Online Pattern Analysis by Evolving Self-Organizing Maps"; example of an algorithm similar to GNG but with different neighborhood function and insertion rule.

- "Topology preserving map formation with a purely local unsupervised competitive learning rule"; example of a Hebbian learning rule with a strong derivation from information-theoretic principles.

- "Kernel-based topographic map formation achieved with an information-theoretic approach"; another example of a Hebbian learning rule with a strong derivation from information-theoretic principles.

- "A Bayesian Analysis of Self-Organising Maps"; a thorough mathematical grounding of SOMs and other Hebbian networks in Bayesian methods; reference if deep rigor is needed for some reason.

### main.2 - Statistical Distances

- "Statistical Distances and Probability Metrics"; defines a generalized Mahalanobis distance that is perfectly suited for use as a fuzzy logical membership function for each scale-space cluster.

### main.4 - Scale-Space

- "Feature Detection with Automatic Scale Selection" and "Real-time Scale Selection in Hybrid Multi-scale Representations"; define a framework for working with scale-spaces; propose definition of most natural choice of features as local maxima in scale-space.

### main.3 - Clustering
- "The Relevant-Set Correlation Model for Data Clustering"; very systematic treatment of clustering; notable for its use of sampling the data at different scales to act as cluster candidate seeds and for its definition of well-founded similarity scores; the similarity scores defined bear some resemblance to the measures of graph conductivity used in max-flow/min-cut algorithms and perhaps a connection could be made?

- "Affinity propagation - Clustering data by passing messages"; proposes a variant of belief propagation for online, dynamical clustering of a dataset; only downside is quadratic dependence on size of set.

## Secondary

### secondary.3 - Spatial Partition Trees

- "Which Spatial Partition Trees are Adaptive to Intrinsic Dimension"; rigorous definition of 'intrinsic dimensionality'; could also use spatial partition trees described herein for baseline performance comparisons with Proteus.
