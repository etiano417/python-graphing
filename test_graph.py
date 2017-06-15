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
        self.assertEquals(self.g.edges, {"e1","e2"})
        self.assertEqual(self.g.incidence, {"e1": ("v1", "v2"), "e2": ("v1", "v1")})


if __name__ == '__main__':
    unittest.main(exit=False)