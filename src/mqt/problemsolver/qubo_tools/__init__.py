# Copyright (c) 2023 - 2026 Chair for Design Automation, TUM
# Copyright (c) 2025 - 2026 Munich Quantum Software Company GmbH
# All rights reserved.
#
# SPDX-License-Identifier: MIT
#
# Licensed under the MIT License

"""A package for generating QUBO formulations automatically from a set of constraints for different problem classes.

It allows users to create a `QuboGenerator` object, and gradually add penalty terms and constraints to it.
When done, the object can be used to construct a QUBO formulation of the project on multiple granularity levels.

## Available Subpackages
- `pathfinder`: This module implements the pathfinding functionalities of the `qubo_tools`.
"""

from __future__ import annotations

# Submodule imports.
from .device import Calibration
from .qubo_generator import QuboGenerator

# Base imports.
from . import pathfinder  # isort: skip

__all__ = [
    "Calibration",
    "QuboGenerator",
    "pathfinder",
]
