import unittest
from graph import find_shortest_path as fsp
from graph import negative_loop as nl


class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(fsp('shortest_path.txt',1,4), (3, [1,2,3,4]))

    def test_2(self):
        self.assertEqual(nl('negative_circle.txt'), [3,4,2,3])

if __name__ == '__main__':
    unittest.main()
