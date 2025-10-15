"""Tests the features of the device representation module."""

from __future__ import annotations

import pytest

from mqt.qubomaker import Calibration


@pytest.fixture
def sample_device_heavy_hex() -> Calibration:
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

    cal = Calibration(
        num_qubits=num_qubits,
        one_qubit=dict.fromkeys(range(num_qubits), 0.99),
        two_qubit=dict.fromkeys(heavy_hex_coupling, 0.99),
        measurement_confidences=dict.fromkeys(range(num_qubits), 0.99),
        basis_gates=["cz", "id", "rx", "rz", "rzz", "sx", "x"],
        t1=dict.fromkeys(range(num_qubits), 0.0001),
        t2=dict.fromkeys(range(num_qubits), 0.0002),
    )
    cal.test_tags = {}  # type: ignore[attr-defined]
    cal.test_tags["longest_hamiltonian_path"] = longest_hamiltonian_path  # type: ignore[attr-defined]
    cal.test_tags["longest_heavy_chain"] = [  # type: ignore[attr-defined]
        12,
        31,
        29,
        27,
        25,
        23,
        21,
        40,
        42,
        44,
        46,
        48,
        50,
        69,
        67,
        65,
        63,
        61,
        59,
        78,
        80,
        82,
        84,
        86,
        88,
        107,
        105,
        103,
        101,
        99,
        97,
        116,
    ]
    return cal


def test_connected_qubit_chain(sample_device_heavy_hex: Calibration) -> None:
    """Tests the computation of the longest hamiltonian path through the device topology.

    Args:
        sample_device_heavy_hex (Calibration): The testing device calibration.
    """
    chain = sample_device_heavy_hex.get_connected_qubit_chain()
    assert chain == sample_device_heavy_hex.test_tags["longest_hamiltonian_path"]  # type: ignore[attr-defined]


def test_heavy_chain(sample_device_heavy_hex: Calibration) -> None:
    """Tests the computation of the longest heavy chain through the device topology.

    Args:
        sample_device_heavy_hex (Calibration): The testing device calibration.
    """
    chain = sample_device_heavy_hex.get_heavy_chain()
    assert chain == sample_device_heavy_hex.test_tags["longest_heavy_chain"]  # type: ignore[attr-defined]


def test_shared_neighbor(sample_device_heavy_hex: Calibration) -> None:
    """Tests the computation of a shared neighbor between two qubits.

    Args:
        sample_device_heavy_hex (Calibration): The testing device calibration.
    """
    assert sample_device_heavy_hex.get_shared_neighbor(0, 2) == 1
    assert sample_device_heavy_hex.get_shared_neighbor(0, 19) == 15
    assert sample_device_heavy_hex.get_shared_neighbor(1, 3) == 2
    assert sample_device_heavy_hex.get_shared_neighbor(124, 105) == 112


def test_from_dict(sample_device_heavy_hex: Calibration) -> None:
    """Tests the deserialization of a Calibration object through the `from_dict` method.

    Args:
        sample_device_heavy_hex (Calibration): The testing device calibration.
    """
    obj = {
        "num_qubits": len(sample_device_heavy_hex.one_qubit),
        "one_qubit": sample_device_heavy_hex.one_qubit,
        "two_qubit": sample_device_heavy_hex.two_qubit,
        "measurement_confidences": sample_device_heavy_hex.measurement_confidences,
        "t1": sample_device_heavy_hex.t1,
        "t2": sample_device_heavy_hex.t2,
    }

    c = Calibration.from_dict(obj, ["cz", "id", "rx", "rz", "rzz", "sx", "x"])
    assert c == sample_device_heavy_hex
