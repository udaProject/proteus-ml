# Proteus

## Overview
A universal machine learning architecture; hierarchical growing competitive neural network that MaxEnt approximates the PDF of high-dimensional distributions induced by data point clouds in terms of the natural scale-space clustering structure, recasts data points in terms of fuzzy membership vectors over the clustering structure, and learns fuzzy predicates in a semi-supervised fashion for classification/accepts fuzzy predicates to constrain generation of virtual data points/accepts fuzzy predicates to constrain querying of real data points.


## Installation

### Version
This project uses Python3.8

### Virtual Environment
It's recommended to use `virtualenv`.

Run `python -m pip install virtualenv`.
Then `cd` to repo directory and run `python -m virtualenv .venv` to create local folder called '.venv' to store virtual environment.
Then run `source .venv/bin/activate` to activate virtualenv.
Run `deactivate` or `source deactivate` at any time to exit virtualenv.

### Packages
After activating virtualenv, run `python -m pip install -r "requirements.txt"`.


## Documentation Site
After installation, run command `mkdocs serve`.


## Testing
Tests managed using the Pytest framework.
Run tests using command `pytest -v`.
Run command `pytest --cov=proteus --cov-report=html` to generate coverage report.
Coverage report can be viewed in documentation site.


## Quick References
- [Pytest Coverage](https://coverage.readthedocs.io/en/coverage-4.3.3/)
