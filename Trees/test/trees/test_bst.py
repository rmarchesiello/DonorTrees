import unittest
from Trees.src.trees.bst_tree import BST
from Trees.src.nodes.bst_node import BSTNode


class TestBST(unittest.TestCase):
    def test_create_empty_tree(self):
        tree = BST()
        self.assertEqual(len(tree), 0)
        self.assertIsNone(tree.root)

    def test_create_tree(self):
        tree = BST()
        tree.add_value(100)
        tree.add_value(80)
        tree.add_value(200)
        tree.add_value(90)
        tree.add_value(70)

        root = BSTNode(100)
        root.leftChild = BSTNode(80)
        root.rightChild = BSTNode(200)
        root.leftChild.leftChild = BSTNode(70)
        root.leftChild.rightChild = BSTNode(90)

        # check if the list of their nodes' values are the same:
        treeNodes = [tree.root.value, tree.root.leftChild.value, tree.root.leftChild.leftChild.value,
                     tree.root.leftChild.rightChild.value,
                     tree.root.rightChild.value]
        rootNodes = [root.value, root.leftChild.value, root.leftChild.leftChild.value,
                     root.leftChild.rightChild.value, root.rightChild.value]

        self.assertEqual(treeNodes, rootNodes)

        cmp_tree = BST(root)
        cmp_tree._num_nodes = 5
        self.assertEqual(tree, cmp_tree)

    def test_tree_not_eq(self):
        tree = BST()
        tree.add_value(100)
        tree.add_value(80)
        tree.add_value(200)
        tree.add_value(90)
        tree.add_value(70)

        root = BSTNode(100)
        root.left = BSTNode(80)
        root.right = BSTNode(200)
        root.left.left = BSTNode(70)
        root.left.right = BSTNode(92)

        cmp_tree = BST(root)
        cmp_tree._num_nodes = 5
        self.assertNotEqual(tree, cmp_tree)


if __name__ == '__main__':
    unittest.main()
