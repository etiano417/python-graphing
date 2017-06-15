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


class TestBadVertices(TestGraphConstruction):
    def setUp(self):
        super(TestBadVertices, self).setUp()
        self.vertices = ["v1","v2","v3"]

    def runTest(self):
        with self.assertRaises(TypeError) as context:
            Graph(self.vertices,self.incidence)

class TestBadIncidence(TestGraphConstruction):
    def setUp(self):
        super(TestBadIncidence, self).setUp()
        self.incidence = {"e1","e2"}

    def runTest(self):
        with self.assertRaises(TypeError) as context:
            Graph(self.vertices, self.incidence)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestBadVertices())
    suite.addTest(TestBadIncidence())
    return suite


if __name__ == '__main__':
    unittest.main(exit=False)