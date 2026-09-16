# Copyright (c) 2023 - 2026 Chair for Design Automation, TUM
# Copyright (c) 2025 - 2026 Munich Quantum Software Company GmbH
# All rights reserved.
#
# SPDX-License-Identifier: MIT
#
# Licensed under the MIT License

from __future__ import annotations

import pytest

from mqt.problemsolver.resource_estimation.error_budget_optimization import evaluate, generate_data, train


@pytest.mark.parametrize("benchmark", ["qft", "ae"])
def test_error_budget_optimization(benchmark: str) -> None:
    total_error_budget = 0.1
    benchmarks_and_sizes = [(benchmark, [3, 4, 5])]
    data = generate_data(
        total_error_budget=total_error_budget,
        number_of_randomly_generated_distributions=10,
        benchmarks_and_sizes=benchmarks_and_sizes,
    )
    assert len(data) == 3
    assert [row["numQubits"] for row in data] == [3, 4, 5]
    for row in data:
        assert row["logical"] + row["t_states"] + row["rotations"] == pytest.approx(total_error_budget)
    model, x_test, y_test = train(data)
    y_pred = model.predict(x_test)
    evaluate(x_test, y_pred, total_error_budget)
    evaluate(x_test, y_test, total_error_budget)
