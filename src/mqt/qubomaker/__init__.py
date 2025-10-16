"""A package for generating QUBO formulations automatically from a set of constraints QUBOs for different problem classes.

It allows users to create a `QuboGenerator` object, and gradually add penalty terms and constraints to it.
When done, the object can be used to construct a QUBO formulation of the project on multiple granularity levels.

## Available Subpackages
- `pathfinder`: This module implements the pathfinding functionalities of the QuboMaker.
"""

from __future__ import annotations

from . import pathfinder
from .device import Calibration
from .graph import Graph
from .qubo_generator import QuboGenerator
from .utils import optimize_classically, print_matrix

__all__ = [
    "Calibration",
    "Graph",
    "QuboGenerator",
    "optimize_classically",
    "pathfinder",
    "print_matrix",
]
