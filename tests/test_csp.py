# Copyright (c) 2023 - 2026 Chair for Design Automation, TUM
# Copyright (c) 2025 - 2026 Munich Quantum Software Company GmbH
# All rights reserved.
#
# SPDX-License-Identifier: MIT
#
# Licensed under the MIT License

from __future__ import annotations

from mqt.problemsolver.csp import CSP


def test_csp() -> None:
    csp = CSP()
    sum_s0 = 1
    sum_s1 = 3
    sum_s2 = 3
    sum_s3 = 1
    list_of_constraints = csp.get_kakuro_constraints(sum_s0=sum_s0, sum_s1=sum_s1, sum_s2=sum_s2, sum_s3=sum_s3)
    res = csp.solve(constraints=list_of_constraints, quantum_algorithm="Grover")
    assert res == (0, 3, 1, 0)

    sum_s0 = 3
    sum_s1 = 5
    sum_s2 = 3
    sum_s3 = 5
    list_of_constraints = csp.get_kakuro_constraints(sum_s0=sum_s0, sum_s1=sum_s1, sum_s2=sum_s2, sum_s3=sum_s3)
    res = csp.solve(constraints=list_of_constraints, quantum_algorithm="Grover")
    assert res == (0, 3, 3, 2)
