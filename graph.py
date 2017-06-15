from collections import Counter
"""Graphs and graph functions.

This module offers a collection of graph classes and graph-related functions. These classes and functions are intended
to offer a mathematically accurate tool for graph creation, manipulation, and analysis.

Classes:
    Graph: edges mapped onto vertices.
"""

class Graph:
    """A set of edges mapped onto a set of vertices with an incidence map

    This represents a set of vertices, and an incidence map that maps edges to vertices. The sets of vertices
    and edges are disjoint. The incidence map's keys are edges, and it only includes 2 element Counters
    (representing unordered pairs) as values. These Counters include only vertices.
    """

    def __init__(self, vertices = set(), incidence = dict()):

        if not vertices.isdisjoint(incidence.keys()):
            raise ValueError("vertices and edges must be disjoint")
        #make sure each counter contains a total of 2
        for e in incidence.values():
            if len(e) != 2:
                raise ValueError("each edge in incidence needs exactly two end vertices")

        self._vertices = vertices
        self._incidence = incidence

    @property
    def vertices(self):
        return self._vertices

    @property
    def edges(self):
        return self._incidence.keys

    @property
    def incidence(self):
        return self._incidence



