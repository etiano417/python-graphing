"""Graphs and graph functions.

This module offers a collection of graph classes and graph-related functions. These classes and functions are intended
to offer a mathematically accurate tool for graph creation, manipulation, and analysis.

Classes:
    Graph: edges mapped onto vertices.
"""

class Graph:
    """A set of edges mapped onto a set of vertices with an incidence map

    This represents a set of vertices, a set of edges, and an incidence map that connects the two. The sets of vertices
    and edges are disjoint. The incidence map only includes edges as keys, and it only includes 2 element Counters
    (representing unordered pairs) as values. These Counters include only vertices.
    """

    def __init__(self, vertices = set(), edges = set(), incidence = dict()):
        self._vertices = vertices
        self._edges = edges
        self._incidence = incidence

    def vertices(self):
        return self._vertices

    def edges(self):
        return self._edges

    def incidence(self):
        return self._incidence



