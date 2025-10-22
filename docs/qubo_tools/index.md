---
file_format: mystnb
kernelspec:
  name: python3
mystnb:
  number_source_lines: true
---

# QUBO Tools

`qubo_tools` provides a framework for creating QUBO formulations for diverse optimization problems. These formulations can be used with a wide range of quantum algorithms to find approximate solutions to the problems.

The framework is designed to be user-friendly and to provide a high-level interface for creating QUBO formulations, not requiring any background knowledge in quantum computing or QUBO problems to solve domain-specific problems. It is also designed to be extensible, so that new optimization problems can be added to the framework with relative ease.

Currently, the `qubo_tools` support the following optimization problem types:

- [Pathfinding Problems](pathfinder/index)

In addition to a semantic selection of problem constraints, we also provide a [graphical user interface](pathfinder/GUI) for the Pathfinding submodule, which allows users to interactively define pathfinding problems to be passed to the framework.

The `qubo_tools` support several encoding schemes, allowing end users to easily compare and evaluate different encodings without the need for manual rewriting of the problems.

If you are interested in the theory behind our `qubo_tools`, have a look at the related publication {cite:p}`rovara2024pathfindingframework`.

```{toctree}
:caption: qubo_tools API
:hidden:
:maxdepth: 1

QuboGenerator
pathfinder/index
```
