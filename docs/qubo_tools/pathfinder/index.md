# Pathfinder Submodule

This module implements a `QuboGenerator` for pathfinding problems on directed and undirected graphs in the form of the `PathFindingQuboGenerator` class, a specialization of the general `QuboGenerator` class.

It supports a set of various [constraints](Constraints) that can be used to model a variety of different pathfinding problems.

In addition to that, it also provides three [encoding schemes](Encodings) that can be selected for the construction of QUBO formulations.

Finally, the [GUI](GUI) provides a graphical user interface for the module, which can be used to interactively define pathfinding problems.

In addition to that, the submodule accepts several input formats for the problem instance. A [JSON format](JSON) can be used to define problem constraints and settings. Furthermore, the established [TSPLib format](TSPLib) can be passed to the framework directly, generating the required constraints from the problem instance.

The `PathFindingQuboGenerator` class can be instantiated like this:

```python
import mqt.problemsolver.qubo_tools.pathfinder as pf

...

generator = pf.PathFindingQuboGenerator(
    objective_function=pf.MinimizePathLength(path_ids=[1]),
    graph=graph,
    settings=settings,
)
```

Here, the `objective_function` parameter can represent any objective function for the optimization procedure (`MinimizePathLength` or `MaximizePathLength`). The `graph` parameter is the graph on which the problem is defined. Finally the `settings` parameter is a `PathFindingQuboGeneratorSettings` object that defines settings for the QUBO generator:

- `encoding_type`: The encoding scheme to use for the QUBO formulation.
- `n_paths`: The number of paths to be searched for.
- `max_path_length`: The maximum length of a path.
- `loops`: A boolean value indicating, whether the found paths should be interpreted as loops.

An example settings definition may look like:

```python
import mqt.problemsolver.qubo_tools.pathfinder as pf

settings = pf.PathFindingQuboGeneratorSettings(
    encoding_type=pf.EncodingType.BINARY,
    n_paths=1,
    max_path_length=4,
    loops=False,
)
```

```{toctree}
:caption: Pathfinder
:hidden:
:maxdepth: 1

GUI
JSON
TSPLib
Encodings
Constraints
```
