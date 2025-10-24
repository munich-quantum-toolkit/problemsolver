# JSON Encoding

Instead of using the programming interface for creating a QuboGenerator, the _Pathfinder_ submodule also supports a JSON format.

With a given input file in JSON format, the QuboGenerator can be created using the following code:

```python
with Path.open("input.json") as file:
    generator_new = pf.PathFindingQuboGenerator.from_json(file.read(), graph)
```

The JSON input contains the definitions of problem constraints to be used for the QUBO formulation, as well as general settings such as the desired encoding choice.

The format for the JSON input is defined as:

```txt
{
    "settings": {
        "encoding": one of ["ONE_HOT", "UNARY", "DOMAIN_WALL", "BINARY"],
        "n_paths": integer,
        "max_path_length": integer,
        "loops": boolean,
    },
    "objective_function": Constraint,
    "constraints": array[Constraint]
}
```

Individual constraints are defined based on their [JSON schema definitions](https://github.com/munich-quantum-toolkit/problemsolver/blob/main/src/mqt/problemsolver/qubo_tools/pathfinder/resources/constraints).
