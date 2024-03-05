import os
import os.path
import mqt.qubomaker as qm
from mqt.qubomaker import Graph
from mqt.qubomaker import pathfinder as pf
import tsplib95

graph = Graph.from_adjacency_matrix([
    [0, 2, 6, 6, 2],
    [5, 0, 1, 7, 8],
    [7, 3, 0, 5, 4],
    [4, 8, 1, 0, 3],
    [9, 6, 7, 2, 0],
])

encoding_type = pf.EncodingType.DOMAIN_WALL
n_paths = 1
max_path_length = graph.n_vertices
loop = True
settings = pf.PathFindingQUBOGeneratorSettings(encoding_type, n_paths, max_path_length, loop)

generator = pf.PathFindingQUBOGenerator(
    objective_function=pf.MinimizePathLength(path_ids=[1]), 
    graph=graph, 
    settings=settings
)

generator.add_constraint(pf.PathIsValid(path_ids=[1]))
generator.add_constraint(pf.PathContainsVerticesExactlyOnce(vertex_ids=graph.all_vertices, path_ids=[1]))
generator.add_constraint(pf.PrecedenceConstraint(1, 3, path_ids=[1]))
generator.add_constraint(pf.PrecedenceConstraint(2, 1, path_ids=[1]))
generator.add_constraint(pf.PrecedenceConstraint(5, 4, path_ids=[1]))

generator.construct_qubo_matrix()