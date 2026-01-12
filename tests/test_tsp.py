# Copyright (c) 2023 - 2026 Chair for Design Automation, TUM
# Copyright (c) 2025 - 2026 Munich Quantum Software Company GmbH
# All rights reserved.
#
# SPDX-License-Identifier: MIT
#
# Licensed under the MIT License

from __future__ import annotations

from mqt.problemsolver.tsp import TSP


def test_kakuro() -> None:
    tsp = TSP()
    res = tsp.solve(1, 2, 3, 4, 5, 6, quantum_algorithm="QPE", objective_function="shortest_path")
    assert res is not None
    assert res == [3, 1, 2, 4]
    res = tsp.solve(6, 9, 2, 1, 8, 4, quantum_algorithm="QPE", objective_function="shortest_path")
    assert res is not None
    assert res == [4, 1, 2, 3]
