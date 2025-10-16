"""Represents device information and utility methods for quantum devices."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Calibration:
    """Represents a device calibration including its qubit connectivities and gate fidelities."""

    num_qubits: int

    one_qubit: dict[int, float]
    two_qubit: dict[tuple[int, int], float]
    measurement_confidences: dict[int, float]
    basis_gates: list[str]

    connections_dict: dict[int, list[int]] = field(init=False)
    heavy: dict[int, list[int]] = field(init=False)
    heavy_children: dict[int, list[int]] = field(init=False)

    t1: dict[int, float]
    t2: dict[int, float]

    def __post_init__(self) -> None:
        """Post-initialization to set up connections and heavy nodes."""
        self.connections_dict = {}
        for i, j in self.two_qubit:
            if i not in self.connections_dict:
                self.connections_dict[i] = []
            if j not in self.connections_dict:
                self.connections_dict[j] = []
            self.connections_dict[i].append(j)
            self.connections_dict[j].append(i)
        self.heavy = {}
        self.heavy_children = {}
        for qubit, connections in self.connections_dict.items():
            if len(connections) > 2:
                self.heavy[qubit] = connections
                for connection in connections:
                    if connection not in self.heavy_children:
                        self.heavy_children[connection] = []
                    self.heavy_children[connection].append(qubit)

    def __eq__(self, value: object) -> bool:
        """Check equality between two Calibration objects.

        Args:
            value (object): The other object to compare against.

        Returns:
            bool: True if equal, False otherwise.
        """
        if not isinstance(value, Calibration):
            return False
        return (
            self.num_qubits == value.num_qubits
            and self.one_qubit == value.one_qubit
            and self.two_qubit == value.two_qubit
            and self.measurement_confidences == value.measurement_confidences
            and self.basis_gates == value.basis_gates
            and self.t1 == value.t1
            and self.t2 == value.t2
        )

    def __hash__(self) -> int:
        """Compute a hash for the Calibration object.

        Returns:
            int: The hash value.
        """
        return hash((
            self.num_qubits,
            frozenset(self.one_qubit.items()),
            frozenset(self.two_qubit.items()),
            frozenset(self.measurement_confidences.items()),
            tuple(self.basis_gates),
            frozenset(self.t1.items()),
            frozenset(self.t2.items()),
        ))

    @classmethod
    def from_dict(cls, data: dict[str, Any], basis_gates: list[str]) -> Calibration:
        """Create a Calibration object from a dictionary."""
        return cls(
            num_qubits=data["num_qubits"],
            one_qubit=data["one_qubit"],
            two_qubit=data["two_qubit"],
            measurement_confidences=data["measurement_confidences"],
            basis_gates=basis_gates,
            t1=data["t1"],
            t2=data["t2"],
        )

    def get_shared_neighbor(self, q1: int, q2: int) -> int:
        """Given two qubits in the heavy-hex topology, find a qubit that is connected to both.

        Args:
            q1 (int): The first qubit.
            q2 (int): The second qubit.

        Returns:
            int: The shared neighbor qubit, or -1 if none exists.
        """
        for x in self.connections_dict[q1]:
            if x in self.connections_dict[q2]:
                return x
        return -1

    def get_connected_qubit_chain(self) -> list[int]:
        """Compute the longest possible hamiltonian path through the device topology.

        Returns:
            list[int]: The longest Hamiltonian path through the qubit connectivity graph.
        """
        # To compute the start that leasts to the longest Hamiltonian path, we look for qubits with only one connection.
        # Sometimes, these might not be directly connected to a heavy node, so we keep traversing until we find one that is.
        # That qubit is then the start of the longest Hamiltonian path.
        potential_starts = [x for x in self.connections_dict if len(self.connections_dict[x]) == 1]
        assert len(potential_starts) >= 2, (
            f"There should be exactly two potential starts for the connected qubit chain. ({potential_starts})"
        )
        start = min(potential_starts)

        # To check if `start` is connected to a heavy node, we check whether its successor has more than two connections.
        # Otherwise, we proceed to the successor.
        def get_next(current: int, previous: int) -> int:
            """Compute the next qubit in the chain.

            Args:
                current (int): The current qubit to find the successor for.
                previous (int): The previous qubit in the chain.

            Returns:
                int: The next qubit in the chain, or -1 if none exists.
            """
            for x in self.connections_dict[current]:
                if x != previous:
                    return x
            return -1

        previous = -1
        while len(self.connections_dict[get_next(start, previous)]) == 2:
            p = start
            start = get_next(start, previous)
            previous = p

        # We traverse through the heavy-hex topology to get the longest Hamiltonian path.
        path = [start]
        current = start
        while True:
            possible_successors = [x for x in self.connections_dict[current] if (len(path) == 1 or x != path[-2])]
            successor_distances = sorted([(abs(s - current), s) for s in possible_successors])
            if len(successor_distances) == 0:
                break
            current = successor_distances[0][1]
            path.append(current)
        return path

    def get_heavy_chain(self) -> list[int]:
        """Find a chain of heavy nodes in the heavy-hex topology that are connected through shared children.

        Returns:
            list[int]: A chain of heavy nodes connected through shared children.
        """
        heavy_graph: dict[int, list[int]] = {}
        for x, children in self.heavy.items():
            heavy_graph[x] = []
            for child in children:
                for other in self.heavy_children[child]:
                    if other != x:
                        heavy_graph[x].append(other)
        potential_starts = [x for x in heavy_graph if len(heavy_graph[x]) == 1]
        potential_starts = [x for x in potential_starts if len(heavy_graph[heavy_graph[x][0]]) == 2]

        heavy_chain = [potential_starts[0]]
        while True:
            current = heavy_chain[-1]
            possible_successors = [x for x in heavy_graph[current] if x not in heavy_chain]
            if len(possible_successors) == 0:
                break
            if len(possible_successors) == 1:
                heavy_chain.append(possible_successors[0])
                continue
            assert len(possible_successors) == 2, "Heavy chain must have exactly two successors."
            [s_a, s_b] = possible_successors
            d_a = abs(s_a - current)
            d_b = abs(s_b - current)
            if d_a < d_b:
                heavy_chain.append(s_a)
            else:
                heavy_chain.append(s_b)
        return heavy_chain
