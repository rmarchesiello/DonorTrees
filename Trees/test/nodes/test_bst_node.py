import unittest
from bst_node import BSTNode
from bst_tree import BST


class TestBSTNode(unittest.TestCase):
    def testAttributes(self):
        testNode = BSTNode(5)
        self.assertEqual(testNode.value, 5)

    def testGetRightChild(self):
        pass

    def testGetLeftChild(self):
        pass


if __name__ == '__main__':
    unittest.main()
