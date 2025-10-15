"""This module tests the generation of QAOA circuits (both the standard and heavy-hex optimized variants)."""

from __future__ import annotations

import pytest
import sympy as sp

from mqt.qubomaker import Calibration, QuboGenerator


@pytest.fixture
def simple_generator() -> QuboGenerator:
    """Provides a simple QuboGenerator instance for testing.

    Returns:
        QuboGenerator: An instance of QuboGenerator with the objective function x1 * x2 * x3 * x4 * x5.
    """
    symbols = [sp.Symbol(f"x_{i + 1}") for i in range(5)]
    obj = sp.Mul(*symbols)
    generator = QuboGenerator(obj)
    generator.disable_caching = True
    return generator


@pytest.fixture
def simple_device() -> Calibration:
    """Provides a test device calibration with 500 qubits and nearest-neighbor connectivity."""
    heavy_hex_coupling = []

    def get_qubit_index(row: int, cell: int, off: bool) -> int:
        """Converts a (row, cell, off) tuple to a qubit index.

        Args:
            row (int): The row of the qubit.
            cell (int): The cell of the qubit.
            off (bool): Whether the qubit is in a main row or an off row.

        Returns:
            int: The qubit index.
        """
        if not off:
            return 19 * row + cell
        return 19 * row + 15 + cell

    for row in range(7):
        for cell in range(15):
            current = get_qubit_index(row, cell, False)
            if cell != 14:
                neighbor = get_qubit_index(row, cell + 1, False)
                heavy_hex_coupling.append((current, neighbor))
            if cell % 4 == 0:
                if row % 2 == 0 and row != 6:
                    below = get_qubit_index(row, cell // 4, True)
                    heavy_hex_coupling.append((current, below))
                elif row % 2 == 1:
                    above = get_qubit_index(row - 1, cell // 4, True)
                    heavy_hex_coupling.append((current, above))
            if cell % 4 == 2:
                if row % 2 == 0 and row != 0:
                    above = get_qubit_index(row - 1, cell // 4, True)
                    heavy_hex_coupling.append((current, above))
                elif row % 2 == 1:
                    below = get_qubit_index(row, cell // 4, True)
                    heavy_hex_coupling.append((current, below))

    longest_hamiltonian_path = []
    for row in range(7):
        for cell in range(15):
            if row == 0 and cell == 0:
                continue  # we skip the first qubit.
            current = get_qubit_index(row, cell if row % 2 == 1 else (14 - cell), False)
            longest_hamiltonian_path.append(current)
        if row != 6:
            longest_hamiltonian_path.append(get_qubit_index(row, 3 if row % 2 == 1 else 0, True))

    num_qubits = max(max(pair) for pair in heavy_hex_coupling) + 1

    return Calibration(
        num_qubits=num_qubits,
        one_qubit=dict.fromkeys(range(num_qubits), 0.99),
        two_qubit=dict.fromkeys(heavy_hex_coupling, 0.99),
        measurement_confidences=dict.fromkeys(range(num_qubits), 0.99),
        basis_gates=["cz", "id", "rx", "rz", "rzz", "sx", "x"],
        t1=dict.fromkeys(range(num_qubits), 0.0001),
        t2=dict.fromkeys(range(num_qubits), 0.0002),
    )


def test_simple_qaoa(simple_generator: QuboGenerator) -> None:
    """Tests the construction of a simple QAOA circuit without qubit reuse and with barriers.

    Args:
        simple_generator (QuboGenerator): A simple QuboGenerator fixture.
    """
    circuit = simple_generator.construct_qaoa_circuit(do_reuse=False, include_barriers=True)
    expected_qubits = 8
    assert circuit.num_qubits == expected_qubits
    ops = circuit.count_ops()
    assert ops["barrier"] == 3
    assert ops["h"] == expected_qubits
    assert ops["rx"] == expected_qubits
    assert ops["rzz"] == 10


def test_simple_qaoa_no_barriers(simple_generator: QuboGenerator) -> None:
    """Tests the construction of a simple QAOA circuit without qubit reuse and without barriers.

    Args:
        simple_generator (QuboGenerator): A simple QuboGenerator fixture.
    """
    circuit = simple_generator.construct_qaoa_circuit(do_reuse=False, include_barriers=False)
    expected_qubits = 8
    assert circuit.num_qubits == expected_qubits
    ops = circuit.count_ops()
    assert "barrier" not in ops
    assert ops["h"] == expected_qubits
    assert ops["rx"] == expected_qubits
    assert ops["rzz"] == 10


def test_qaoa_with_reuse(simple_generator: QuboGenerator) -> None:
    """Tests the construction of a QAOA circuit with qubit reuse and without barriers.

    Args:
        simple_generator (QuboGenerator): A simple QuboGenerator fixture.
    """
    circuit = simple_generator.construct_qaoa_circuit(do_reuse=True, include_barriers=False)
    expected_qubits = 3
    expected_variables = 8
    assert circuit.num_qubits == expected_qubits
    ops = circuit.count_ops()
    assert "barrier" not in ops
    assert ops["h"] == expected_variables
    assert ops["rx"] == expected_variables
    assert ops["reset"] == expected_variables - expected_qubits
    assert ops["rzz"] == 10


def test_heavy_hex_qaoa(simple_generator: QuboGenerator, simple_device: Calibration) -> None:
    """Tests the construction of a heavy-hex optimized QAOA circuit.

    Args:
        simple_generator (QuboGenerator): A simple QuboGenerator fixture.
        simple_device (Calibration): A simple device (heavy-hex) calibration fixture.
    """
    circuit = simple_generator.construct_embedded_qaoa_circuit(simple_device)
    assert circuit.num_qubits == simple_device.num_qubits
    ops = circuit.count_ops()
    expected_variables = 8
    assert ops["h"] == expected_variables
    assert ops["rx"] == expected_variables
    assert ops["rzz"] == 10
