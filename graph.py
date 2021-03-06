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

        #make sure no element is both an edge and a vertex
        if not vertices.isdisjoint(incidence.keys()):
            raise ValueError("vertices and edges must be disjoint")
        #make sure each counter contains a total of 2
        for e in incidence.values():
            if len(e) != 2:
                raise ValueError("each edge in incidence needs exactly two end vertices")
        #make sure each edge's endpoints are all vertices
        for e in incidence.values():
            for i in e:
                if i not in vertices:
                    raise ValueError("each edge in incidence needs exactly two end vertices")

        self._vertices = vertices
        self._incidence = incidence

    @property
    def vertices(self):
        return self._vertices

    @property
    def edges(self):
        edge_iterator = iter(self._incidence.keys())
        return set(edge_iterator)

    @property
    def incidence(self):
        return self._incidence

    def incident(self, element):

        output = set()

        if element in self.vertices:
            for edge in self._incidence:
                if element in self._incidence[edge]:
                    output.add(edge)

        elif element in self.edges:
            end_vertices = self._incidence[element]
            output = set(end_vertices)

        else:
            raise ValueError("element "+element+" not in graph")

        return output

    def parallel(self, edge):
        if edge in self.vertices:
            raise ValueError("given element must be an edge")
        end_points = self.incident(edge)

        output = set()

        for element in self.edges:
            if self.incident(element) == end_points:
                output.add(element)

        output.remove(edge)

        return output

    def is_loop(self, edge):
        if edge not in self.edges:
            raise ValueError("given element must be an edge")

        end_points = self.incident(edge)
        return len(end_points) == 1

    def closed_neighborhood(self, vertex):
        if vertex not in self.vertices:
            raise ValueError("given element must be a vertex")

        output = set()

        for edge in self.incident(vertex):
            output = output.union(self.incident(edge))

        #even though the previous operation will add the given vertex to the
        #output set if it has any incident edges at all, it will fail to do
        #so in the case of an isolated vertex.
        output = output.union({vertex})

        return output

    def open_neighborhood(self, vertex):
        closed_n = self.closed_neighborhood(vertex)
        return closed_n.difference({vertex})

