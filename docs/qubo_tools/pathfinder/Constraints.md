---
file_format: mystnb
kernelspec:
  name: python3
mystnb:
  number_source_lines: true
---

# Constraints

The _Pathfinder_ submodule supports a total of 13 constraints. These constraints are translated
into their QUBO formulation automatically during the QUBO generation process, based on the selected encoding.

The following lists all supported constraints together with their properties and their QUBO formulations.
In the formula representation, $\delta(x, v, i, \pi^{(i)})$ is a function that returns 1 if vertex $v$ is at position $i$ of path $\pi^{(i)}$ and 0 otherwise.
The specific function depends on the selected [encoding](Encodings).

In each formula, $x$ is the binary variable assignment, $N$ is the maximum path length, $V$ is the set of vertices, $E$ is the set of edges, and $A_{uv}$ is the adjacency matrix of the graph.

## PathIsValid

Enforces that a path is valid. A path is valid if:

#. For any two consecutive vertices, there exists an edge between them.
#. If the used encoding is `ONE_HOT`, no two or more vertices are selected as the same position of the same path.
#. If the used encoding is `DOMAIN_WALL`, the bitstring indicating the vertex occupying position $j$ of path $\pi^{(i)}$ is of the form $111..10..0$, i.e. after the first 0, no more bits have the value 1.

Properties:

- `path_ids: list[int]`: A list of IDs of the paths this constraint should be applied to.

$$ \sum*{(u \rightarrow v) \not \in E} \sum*{i = 1}^{N} \delta(x, \pi, u, i) \delta(x, \pi, v, i+1)$$

_Encoding-specific penalties are further added to this expression if necessary._

## PathPositionIs

Enforces that a given position of a provided path is occupied by one of a set of vertices.

Properties:

- `position: int`: The position of the path subject to this constraint.
- `vertex_ids: list[int]`: A list of IDs of the vertices that can occupy the position.
- `path: int`: The ID of the path this constraint should be applied to.

$$1 -  \sum_{v  \in V'}  \delta(x,  \pi, v, i)$$

## PathStartsAt

Enforces that a given path starts at one of a given set of vertices.

Properties:

- `vertex_ids: list[int]`: A list of IDs of the vertices that the path can start at.
- `path: int`: The ID of the path this constraint should be applied to.

$$1 -  \sum_{v  \in V'}  \delta(x,  \pi, v, 1)$$

## PathEndsAt

Enforces that a given path ends at one of a given set of vertices.

Properties:

- `vertex_ids: list[int]`: A list of IDs of the vertices that the path can end at.
- `path: int`: The ID of the path this constraint should be applied to.

$$ \sum*{i=2}^N \left[ \left(1 - \sum*{v \in V} \delta(x, \pi, v, i) \right)^2 \left( \sum*{v \not \in V'} \delta(x, \pi, v, i - 1) \right) \right] + \sum*{v \not \in V'} \delta(x, \pi, v, N)$$

## PathContainsVerticesExactlyOnce

Enforces that a given set of paths each contain each given vertex exactly once.

Properties:

- `vertex_ids: list[int]`: A list of IDs of the vertices that should be contained exactly once in each path.
- `path_ids: list[int]`: A list of IDs of the paths this constraint should be applied to.

$$ \left(1 - \sum\_{i = 1}^N \delta(x, \pi, v, i) \right) ^2$$

## PathContainsVerticesAtLeastOnce

Enforces that a given set of paths each contain each given vertex at least once.

Properties:

- `vertex_ids: list[int]`: A list of IDs of the vertices that should be contained at least once in each path.
- `path_ids: list[int]`: A list of IDs of the paths this constraint should be applied to.

$$ \prod\_{i=1}^N(1 - \delta(x, v, i))$$

## PathContainsVerticesAtMostOnce

Enforces that a given set of paths each contain each given vertex at most once.

Properties:

- `vertex_ids: list[int]`: A list of IDs of the vertices that should be contained at most once in each path.
- `path_ids: list[int]`: A list of IDs of the paths this constraint should be applied to.

$$ \sum\_{1 \leq i \lt j \lt N} \delta(x, v,i) \delta(x, v,j)$$

## PathContainsEdgesExactlyOnce

Enforces that a given set of paths each contain each given edge exactly once.

Properties:

- `edges: list[tuple[int, int]]`: A list of the edges that should be contained exactly once in each path.
- `path_ids: list[int]`: A list of IDs of the paths this constraint should be applied to.

$$ \left( 1 - \sum\_{i=1}^{N} \delta(x, \pi, u, i) \delta(x, \pi, v, i + 1) \right)^2$$

## PathContainsEdgesAtLeastOnce

Enforces that a given set of paths each contain each given edge at least once.

Properties:

- `edges: list[tuple[int, int]]`: A list of the edges that should be contained at least once in each path.
- `path_ids: list[int]`: A list of IDs of the paths this constraint should be applied to.

$$ \prod\_{i=1}^N(1 - \delta(x, \pi, u, i) \delta(x, \pi, v, i +1))$$

## PathContainsEdgesAtMostOnce

Enforces that a given set of paths each contain each given edge at most once.

Properties:

- `edges: list[tuple[int, int]]`: A list of the edges that should be contained at most once in each path.
- `path_ids: list[int]`: A list of IDs of the paths this constraint should be applied to.

$$ \sum\_{1 \leq i \lt j \leq N}( \delta(x, \pi, u, i) \delta(x, \pi, v,i+1))( \delta(x, \pi, u,j) \delta(x, \pi, v,j+1))$$

## PrecedenceConstraint

For the given vertices $u$ and $v$, enforces that $u$ is visited before $v$ in the path.

Properties:

- `pre: int`: The ID of the preceding vertex.
- `post: int`: The ID of the preceded vertex.

$$ \sum*{i=1}^N \delta(x, \pi, v,i) \prod*{j=1}^{i-1}(1- \delta(x, \pi, u,j))$$

## PathsShareNoVertices

Enforces that two given paths share no vertices.

Properties

- `path_one: int`: The ID of the first path.
- `path_two: int`: The ID of the second path.

$$ \sum*{v \in V} \left[ \left( \sum*{i=1}^N \delta(x, \pi^{(1)}, v, i) \right) \left( \sum\_{i=1}^N \delta(x, \pi^{(2)}, v, i) \right) \right]$$

## PathsShareNoEdges

Enforces that two given paths share no edges.

Properties

- `path_one: int`: The ID of the first path.
- `path_two: int`: The ID of the second path.

$$ \sum*{(u \rightarrow v) \in E} \left[ \left( \sum*{i=1}^{N} \delta(x, \pi^{(1)}, u, i) \delta(x, \pi^{(1)}, v, i + 1) \right) \left( \sum\_{i=1}^{N} \delta(x, \pi^{(2)}, u, i) \delta(x, \pi^{(2)}, v, i + 1) \right) \right]$$

## MinimizePathLength

Enforces that the length of a given path is minimized.

Properties

- `path_ids: list[int]`: The IDs of the paths this constraint should be applied to.

$$ \sum*{(u \rightarrow v) \in E} \sum*{i = 1}^{N} A\_{uv} \delta(x, \pi, u, i) \delta(x, \pi, v, i+1)$$

## MaximizePathLength

Enforces that the length of a given path is maximized.

Properties

- `path_ids: list[int]`: The ID of the paths this constraint should be applied to.

$$- \sum_{(u  \rightarrow v)  \in E}  \sum_{i = 1}^{N} A_{uv} \delta(x,  \pi, u, i) \delta(x,  \pi, v, i+1)$$
