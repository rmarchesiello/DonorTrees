import unittest
from bst_node import BSTNode
from bst_tree import BST


class TestBSTNode(unittest.TestCase):
    def testAttributes(self):
        testNode = BSTNode(5)
        self.assertEqual(testNode.value, 5)

    def testGetrightWithNoChildren(self):
        testNode = BSTNode(10)
        self.assertEqual(testNode.getright(), -1)

    def testGetrightWithChildren(self):
        testNode = BSTNode(15)
        testNode.right = 20
        self.assertEqual(testNode.getright(), 20)

    def testGetleftWithNoChildren(self):
        testNode = BSTNode(20)
        self.assertEqual(testNode.getleft(), -1)

    def testGetleftWithChildren(self):
        testNode = BSTNode(50)
        testNode.left = 10
        self.assertEqual(testNode.getleft(), 10)

    def testNumChildrenWithNoChildren(self):
        testNode = BSTNode(15)
        self.assertEqual(testNode.numChildren(), 0)

    def testNumChildrenWithOneChild(self):
        testNode = BSTNode(15)
        testNode.left = 10

        self.assertEqual(testNode.left, 10)

    def testNumChildrenWithTwoChildren(self):
        testNode = BSTNode(15)
        testNode.left = 10
        testNode.right = 30

        self.assertEqual(testNode.left, 10)
        self.assertEqual(testNode.right, 30)


if __name__ == "__main__":
    unittest.main()
