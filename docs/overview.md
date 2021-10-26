## Overview
A universal machine learning architecture; hierarchical growing competitive neural network that MaxEnt approximates the PDF of high-dimensional distributions induced by data point clouds in terms of the natural scale-space clustering structure, recasts data points in terms of fuzzy membership vectors over the clustering structure, and learns fuzzy predicates in a semi-supervised fashion for classification/accepts fuzzy predicates to constrain generation of virtual data points/accepts fuzzy predicates to constrain querying of real data points.

### Requirements
- Input dimensions of data will have to be continuous and bounded, so they can be mapped to the range [0,1] of reals
