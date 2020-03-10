import unittest
from bst_node import BSTNode
from bst_tree import BST


class TestBSTNode(unittest.TestCase):
    def testAttributes(self):
        testNode = BSTNode(5)
        self.assertEqual(testNode.value, 5)

    def testGetRightChildWithNoChildren(self):
        testNode = BSTNode(10)
        self.assertEqual(testNode.getRightChild(), -1)

    def testGetRightChildWithChildren(self):
        testNode = BSTNode(15)
        testNode.rightChild = 20
        self.assertEqual(testNode.getRightChild(), 20)

    def testGetLeftChildWithNoChildren(self):
        testNode = BSTNode(20)
        self.assertEqual(testNode.getLeftChild(), -1)

    def testGetLeftChildWithChildren(self):
        testNode = BSTNode(50)
        testNode.leftChild = 10
        self.assertEqual(testNode.getLeftChild(), 10)

    def testNumChildrenWithNoChildren(self):
        testNode = BSTNode(15)
        self.assertEqual(testNode.numChildren(), 0)

    def testNumChildrenWithOneChild(self):
        testNode = BSTNode(15)
        testNode.leftChild = 10
        testNode.children[0] = testNode.leftChild
        self.assertEqual(testNode.numChildren(), 1)

    def testNumChildrenWithTwoChildren(self):
        testNode = BSTNode(15)
        testNode.leftChild = 10
        testNode.rightChild = 30

        testNode.children[0] = testNode.leftChild
        testNode.children[1] = testNode.rightChild
        self.assertEqual(testNode.numChildren(), 2)

if __name__ == "__main__":
    unittest.main()