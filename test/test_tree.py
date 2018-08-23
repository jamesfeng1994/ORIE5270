from tree.tree_print import Tree
from tree.tree_print import Node
import unittest


class TestStringMethods(unittest.TestCase):

    def test_1(self):
        a = Node('1', None, None)

        tree = Tree(a)
        ans = [['1']]

        self.assertEqual(tree.print_tree(), ans)

    def test_2(self):
        a = Node('1', None, None)
        b = Node('2', None, None)
        c = Node('3', None, None)
        d = Node('4', None, None)
        e = Node('5', None, None)
        f = Node('6', None, None)
        g = Node('7', None, None)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.left = f
        c.right = g

        tree = Tree(a)
        ans = [['|', '|', '|', '1', '|', '|', '|'],
               ['|', '2', '|', '|', '|', '3', '|'],
               ['4', '|', '5', '|', '6', '|', '7']]

        self.assertEqual(tree.print_tree(), ans)

    def test_3(self):
        a = Node('1', None, None)
        b = Node('2', None, None)
        c = Node('3', None, None)
        d = Node('4', None, None)

        a.left = b
        b.left = c
        c.left = d

        tree = Tree(a)
        ans = [['|', '|', '|', '|', '|', '|', '|', '1', '|', '|', '|', '|', '|', '|', '|'],
               ['|', '|', '|', '2', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|'],
               ['|', '3', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|'],
               ['4', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|']]

        self.assertEqual(tree.print_tree(), ans)

    def test_4(self):
        a = Node('1', None, None)
        b = Node('2', None, None)
        c = Node('3', None, None)
        d = Node('4', None, None)
        e = Node('5', None, None)
        f = Node('6', None, None)

        a.left = b
        a.right = c
        b.right = d
        c.left = e
        e.right = f

        tree = Tree(a)
        ans = [['|', '|', '|', '|', '|', '|', '|', '1', '|', '|', '|', '|', '|', '|', '|'],
               ['|', '|', '|', '2', '|', '|', '|', '|', '|', '|', '|', '3', '|', '|', '|'],
               ['|', '|', '|', '|', '|', '4', '|', '|', '|', '5', '|', '|', '|', '|', '|'],
               ['|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '6', '|', '|', '|', '|']]

        self.assertEqual(tree.print_tree(), ans)


if __name__ == '__main__':
    unittest.main()
