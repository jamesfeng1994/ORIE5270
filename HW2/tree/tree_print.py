class Tree(object):

    def __init__(self, root):
        self.root = root

    def get_depth(self, current, n):
        """
        This function is to get the depth of the tree using recursion
        parameters: 
            current: current tree node
            n: current level of the tree
        return: the depth of the tree
        """
        if current is not None:
            return max(self.get_depth(current.left, n + 1), self.get_depth(current.right, n + 1))
        else:
            return n

    def traverse_tree(self, current, n, tree_list):
        """
        This function is to traverse the tree and store keys of tree nodes
        parameters:
            current: current tree node
            n: current tree level
            tree_list: a list storing keys of tree nodes (from parents to kids)
        return: a list storing all nodes' keys (from root to leaves)
        """
        depth = self.get_depth(self.root, 0)

        if n == 0:
            tree_list = [[] for i in range(depth)]

        tree_list[n].append(current.value)

        if current.left is not None:
            tree_list = self.traverse_tree(current.left, n + 1, tree_list)
        elif n < depth - 1:
            tree_list[n + 1].append(None)

        if current.right is not None:
            tree_list = self.traverse_tree(current.right, n + 1, tree_list)
        elif n < depth - 1:
            tree_list[n + 1].append(None)

        return tree_list

    def print_tree(self):
        """
        This function is to print the tree by returning a matrix
        return: a matrix representing the tree
        """
        tree_list = self.traverse_tree(self.root, 0, [])
        depth = self.get_depth(self.root, 0)

        for i in range(depth - 1):
            for j in range(len(tree_list[i])):
                if tree_list[i][j] is None:
                    tree_list[i + 1].insert(2 * j, None)
                    tree_list[i + 1].insert(2 * j + 1, None)

        tree_matrix = [['|' for i in range(2 ** depth - 1)] for j in range(depth)]
        for i in range(depth):
            for j in range(len(tree_list[i])):
                if tree_list[i][j] is not None:
                    tree_matrix[i][2 ** (depth - i - 1) - 1 + j * 2 ** (depth - i)] = tree_list[i][j]
        return tree_matrix


class Node(object):

    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
