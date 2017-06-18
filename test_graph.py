import unittest
from collections import Counter
from graph import Graph


class TestGraphConstruction(unittest.TestCase):
    def setUp(self):
        self.vertices = {"v1", "v2", "v3"}
        end_vertices_1 = ("v1", "v2")
        end_vertices_2 = ("v1", "v1")
        self.incidence = {"e1": end_vertices_1, "e2": end_vertices_2}

    def runTest(self):
        g = Graph(self.vertices,self.incidence)


class TestBadVerticesType(TestGraphConstruction):
    def setUp(self):
        super(TestBadVerticesType, self).setUp()
        self.vertices = ["v1","v2","v3"]

    def runTest(self):
        with self.assertRaises(AttributeError) as context:
            Graph(self.vertices,self.incidence)


class TestBadIncidenceType(TestGraphConstruction):
    def setUp(self):
        super(TestBadIncidenceType, self).setUp()
        self.incidence = {"e1","e2"}

    def runTest(self):
        with self.assertRaises(AttributeError) as context:
            Graph(self.vertices, self.incidence)


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.vertices = {"v1", "v2", "v3"}
        end_vertices_1 = ("v1", "v2")
        end_vertices_2 = ("v1", "v1")
        self.incidence = {"e1": end_vertices_1, "e2": end_vertices_2}
        self.g = Graph(self.vertices, self.incidence)

    def runTest(self):
        self.assertEquals(self.g.vertices, {"v1", "v2", "v3"})
        self.assertEquals(self.g.edges, {"e1", "e2"})
        self.assertEqual(self.g.incidence, {"e1": ("v1", "v2"), "e2": ("v1", "v1")})


class TestSimpleGraph(unittest.TestCase):
    def setUp(self):
        self.vertices = {"v1"}
        self.g = Graph(self.vertices)

    def runTest(self):
        self.assertEquals(self.g.vertices, {"v1"})
        self.assertEquals(self.g.edges, set())
        self.assertEqual(self.g.incidence, dict())


class TestIncidentVertices(TestGraph):
    def runTest(self):
        self.assertEqual(self.g.incident("v1"),{"e1","e2"})
        self.assertEqual(self.g.incident("v2"), {"e1"})


class TestIncidentVerticesSimple(TestSimpleGraph):
    def runTest(self):
        self.assertEqual(self.g.incident("v1"),set())


class TestIncidentEdges(TestGraph):
    def runTest(self):
        self.assertEqual(self.g.incident("e1"), {"v1", "v2"})
        self.assertEqual(self.g.incident("e2"), {"v1"})


class TestGraphParallelEdges(unittest.TestCase):
    def setUp(self):
        vertices = {"v1","v2","v3"}
        end_vertices_1 = ("v1", "v2")
        end_vertices_2 = ("v1", "v2")
        end_vertices_3 = ("v1", "v1")
        end_vertices_4 = ("v1", "v1")
        end_vertices_5 = ("v1", "v2")
        end_vertices_6 = ("v1", "v3")
        incidence = {"e1": end_vertices_1, "e2": end_vertices_2, "e3": end_vertices_3, "e4": end_vertices_4,
                     "e5": end_vertices_5, "e6": end_vertices_6}
        self.g = Graph(vertices,incidence)


class TestParallelFalse(TestGraphParallelEdges):
    def runTest(self):
        self.assertEquals(self.g.parallel("e6"),set())
        with self.assertRaises(ValueError) as context:
            self.g.parallel("v1")


class TestParallel(TestGraphParallelEdges):
    def runTest(self):
        x = self.g.parallel("e1")
        self.assertEqual(self.g.parallel("e1"),{"e2","e5"})
        self.assertEqual(self.g.parallel("e3"), {"e4"})


if __name__ == '__main__':
    unittest.main(exit=False)