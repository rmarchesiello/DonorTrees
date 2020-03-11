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
        root.left = BSTNode(80)
        root.right = BSTNode(200)
        root.left.left = BSTNode(70)
        root.left.right = BSTNode(90)

        cmp_tree = BST(root)
        self.assertEqual(tree, cmp_tree)  # but we don't pass this

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

    def testRemoveValueWithNoChildren(self):
        tree = BST()
        tree.add_value(100)
        tree.add_value(50)
        tree.add_value(125)
        tree.add_value(200)

        otherTree = BST()
        otherTree.add_value(100)
        otherTree.add_value(50)
        otherTree.add_value(125)

        # remove a leaf node (a node with no children)
        tree.remove_value(200)

        self.assertEqual(tree, otherTree)

    def testRemoveValueWithNoChildrenXD(self):
        tree = BST()
        tree.add_value(250)
        tree.add_value(225)
        tree.add_value(275)

        otherTree = BST()
        otherTree.add_value(250)
        otherTree.add_value(275)

        # remove a left leaf
        tree.remove_value(225)
        self.assertEqual(tree, otherTree)

    def testRemoveValueWithOneChildLeftSide(self):
        tree = BST()
        tree.add_value(100)
        tree.add_value(50)
        tree.add_value(200)
        tree.add_value(25)

        otherTree = BST()
        otherTree.add_value(100)
        otherTree.add_value(25)
        otherTree.add_value(200)

        # remove value 25 from tree and compare to otherTree
        tree.remove_value(50)

        self.assertEqual(tree, otherTree)

    def testRemoveValueWithOneChildRightSide(self):
        tree = BST()
        tree.add_value(100)
        tree.add_value(50)
        tree.add_value(125)
        tree.add_value(200)

        otherTree = BST()
        otherTree.add_value(100)
        otherTree.add_value(50)
        otherTree.add_value(200)

        # remove value 125 from tree and compare to otherTree
        tree.remove_value(125)

        self.assertEqual(tree, otherTree)

    def testRemoveValueWithTwoChildren(self):
        tree = BST()
        tree.add_value(300)
        tree.add_value(250)
        tree.add_value(500)
        tree.add_value(225)
        tree.add_value(275)

        otherTree = BST()
        otherTree.add_value(275)
        otherTree.add_value(250)
        otherTree.add_value(500)
        otherTree.add_value(225)

        # tree.printPreorder(root=tree.root)
        # print(tree.__len__()) ## should print 13
        #
        tree.remove_value(300)
        # print()
        # tree.printPreorder(root=tree.root)
        # print(tree.__len__()), ## should print 12

        self.assertEqual(tree, otherTree)
        # treeLength =
        self.assertEqual(tree.__len__(), otherTree.__len__())

    def testRemoveValueInnerNodeWithTwoChildren(self):
        # removing an inner node with two children- node with a value of 250
        tree = BST()
        tree.add_value(300)
        tree.add_value(250)
        tree.add_value(500)
        tree.add_value(225)
        tree.add_value(275)

        otherTree = BST()
        otherTree.add_value(300)
        otherTree.add_value(500)
        otherTree.add_value(225)
        otherTree.add_value(275)

        tree.remove_value(250)

        self.assertEqual(tree, otherTree)

    def testRemoveValueWeirdTree(self):
        tree = BST()
        tree.add_value(100)
        tree.add_value(50)
        tree.add_value(150)
        tree.add_value(125)
        tree.add_value(120)
        tree.add_value(125)
        tree.add_value(127)
        tree.add_value(126)

        otherTree = BST()
        otherTree.add_value(100)
        otherTree.add_value(50)
        otherTree.add_value(150)
        otherTree.add_value(125)
        otherTree.add_value(120)
        otherTree.add_value(125)
        otherTree.add_value(126)

        # remove 127 from tree
        tree.remove_value(127)
        self.assertEqual(tree, otherTree)

    def testGetMaxNode(self):
        tree = BST()
        tree.add_value(50)
        tree.add_value(25)
        tree.add_value(100)
        tree.add_value(10)
        tree.add_value(150)

        maxNode = tree.get_max_node()
        self.assertEqual(maxNode.value, 150)

    def testGetMinNode(self):
        tree = BST()
        tree.add_value(50)
        tree.add_value(25)
        tree.add_value(100)
        tree.add_value(10)
        tree.add_value(150)

        minNode = tree.get_min_node()
        self.assertEqual(minNode.value, 10)

    def testHeight(self):
        tree = BST()
        tree.add_value(50)
        tree.add_value(25)
        tree.add_value(100)
        tree.add_value(10)
        tree.add_value(150)

        heightOfTree = tree.height

        self.assertEqual(heightOfTree, 2)

    def testGetNode(self):
        tree = BST()
        tree.add_value(200)
        tree.add_value(100)
        tree.add_value(300)
        tree.add_value(50)
        tree.add_value(110)
        tree.add_value(250)
        tree.add_value(500)
        tree.add_value(25)
        tree.add_value(75)
        tree.add_value(105)
        tree.add_value(150)
        tree.add_value(225)
        tree.add_value(275)

        retrievedNode = tree.get_node(105)
        self.assertEqual(retrievedNode.value, 105)


if __name__ == '__main__':
    unittest.main()
