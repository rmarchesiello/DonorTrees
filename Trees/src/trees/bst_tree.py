from typing import Optional, Callable, TypeVar, Generic

from Trees.src.errors import MissingValueError, EmptyTreeError
from Trees.src.nodes.bst_node import BSTNode
from math import log, floor
import sys

T = TypeVar('T')
K = TypeVar('K')


class BST(Generic[T, K]):
    """
    T: The value stored in the node
    K: The value used in comparing nodes
    """

    def __init__(self, root: Optional[BSTNode[T]] = None, key: Callable[[T], K] = lambda x: x) -> None:
        """
        You must have at least one member named root

        :param root: The root node of the tree if there is one.
        If you are provided a root node don't forget to count how many nodes are in it
        :param key: The function to be applied to a node's value for comparison purposes.
        It serves the same role as the key function in the min, max, and sorted builtin
        functions
        """
        self.root = root  # this should be a BSTNode object
        if key is not None:
            self.key = key  # how a node's value will be ordered in the BST??
        self.length = 0  # keeps track of how many nodes are in the BST
        self.inorderList = []

    @property
    def height(self) -> int:
        """
        Compute the height of the tree. If the tree is empty its height is -1
        :return:
        """
        if self.length == 0:
            return -1
        else:  # I think the height of a BST is log base 2 N; but ill check on that
            return floor(log(self.length)/log(2))

    def __len__(self) -> int:
        """
        :return: the number of nodes in the tree
        """
        return self.length

    def add_value(self, value: T, curNode: BSTNode = None) -> None:
        """
        Add value to this BST
        :param curNode: defaults to None, but is the current node that the algorithm is on
        :param value: the donation amount
        :return: None
        """
        if curNode is None:
            curNode = self.root

        if self.root is None: # base case- tree is empty so create a node and make it the root
            self.root = BSTNode(value)
            self.length = self.length + 1
        elif self.key(value) == self.key(curNode.value):
            if curNode.getRightChild() == -1:
                curNode.rightChild = BSTNode(value, parent = curNode)
                curNode.children[1] = curNode.rightChild
                self.length += 1
            else:
                newNode = curNode.rightChild
                self.add_value(value, newNode)
        elif self.key(value) < self.key(curNode.value):  # I think we have to call key on this??
            if curNode.getLeftChild() == -1:  # in other words, if curNode doesn't have a left child..
                curNode.leftChild = BSTNode(value, parent=curNode)
                curNode.children[0] = curNode.leftChild
                self.length = self.length + 1
            else:
                newNode = curNode.leftChild
                self.add_value(value, newNode)  # recursive call to continue to find the correct spot for entry

        else:  # self.key(value) > self.key(curNode.rightChild):
            if curNode.getRightChild() == -1:
                curNode.rightChild = BSTNode(value, parent=curNode)
                curNode.children[1] = curNode.rightChild
                self.length = self.length + 1
            else:
                self.add_value(value, curNode.rightChild)

    def get_node(self, value: K, curNode: BSTNode = None) -> BSTNode[T]:
        """
        Get the node with the specified value
        :param curNode:
        :param value:
        :raises MissingValueError if there is no node with the specified value
        :return:
        """
        try:
            if curNode is None:
                curNode = self.root

            if self.key(curNode.value) == value:
                return curNode
            elif value < self.key(curNode.value):
                return self.get_node(value, curNode.leftChild)
            elif value > self.key(curNode.value):
                return self.get_node(value, curNode.rightChild)

            else:
                raise RecursionError

        except RecursionError as e:
            raise MissingValueError

    def get_max_node(self) -> BSTNode[T]:
        """
        Return the node with the largest value in the BST
        :return:
        :raises EmptyTreeError if the tree is empty
        """
        curNode = self.root
        while curNode.getRightChild() != -1:
            curNode = curNode.rightChild
        return curNode

    def get_min_node(self) -> BSTNode[T]:
        """
        Return the node with the smallest value in the BST
        :return:
        """
        curNode = self.root
        while curNode.getLeftChild() != -1:
            curNode = curNode.leftChild
        return curNode

    def remove_value(self, value: T) -> None:
        """
        Remove the node with the specified value.
        When removing a node with 2 children take the successor for that node
        to be the largest value smaller than the node (the max of the
        left subtree)
        :param value:
        :return:
        :raises MissingValueError if the node does not exist
        """
        try:
            nodeToRemove = self.get_node(value)
            if nodeToRemove.numChildren() == 0:
                del nodeToRemove
                self.length -= 1

            elif nodeToRemove.numChildren() == 1:
                if nodeToRemove.getRightChild() != -1:
                    temp = nodeToRemove.rightChild
                    curParent = nodeToRemove.parent
                    if nodeToRemove is self.root:
                        self.root = nodeToRemove.rightChild
                        del nodeToRemove
                    elif nodeToRemove is nodeToRemove.parent.leftChild:
                        del nodeToRemove
                        curParent.leftChild = temp
                    elif nodeToRemove is nodeToRemove.parent.rightChild:
                        del nodeToRemove
                        curParent.rightChild = temp
                    self.length -= 1
                else:
                    temp = nodeToRemove.leftChild
                    curParent = nodeToRemove.parent
                    if nodeToRemove is self.root:
                        self.root = nodeToRemove.leftChild
                        del nodeToRemove
                    elif nodeToRemove is nodeToRemove.parent.rightChild:
                        del nodeToRemove
                        curParent.rightChild = temp
                    elif nodeToRemove is nodeToRemove.parent.leftChild:
                        del nodeToRemove
                        curParent.leftChild = temp
                    self.length -= 1
            elif nodeToRemove.numChildren() == 2:
                curNode = nodeToRemove.rightChild
                while curNode.getLeftChild() != -1:
                    curNode = curNode.leftChild
                nodeToRemove.value = curNode.value
                del curNode
                self.length -= 1
        except MissingValueError:
            print("value you are trying to remove does not exist!")

    def printPreorder(self, root):
        if root:
            print(root.value)
            self.printPreorder(root.leftChild)
            self.printPreorder(root.rightChild)

    def printInorder(self, root, reverse = False):
        if reverse == False:
            if root:
                self.printInorder(root.leftChild)
                print(root.value)
                self.printInorder(root.rightChild)
        else:
            if root:
                self.printInorder(root.rightChild)
                print(root.value)
                self.printInorder(root.leftChild)

    def storeInorder(self, root):
        if root:
            self.storeInorder(root.leftChild)
            self.inorderList.append(root.value)
            self.storeInorder(root.rightChild)

    def printPostorder(self, root):
        if root:
            self.printPostorder(root.leftChild)
            self.printPostorder(root.rightChild)
            print(root.value)

    def __eq__(self, other: object) -> bool:
        if self is other:
            return True
        elif isinstance(other, BST):
            if len(self) == 0 and len(other) == 0:
                return True
            else:
                return len(self) == len(other) and self.root.value == other.root.value and \
                       BST(self.root.left) == BST(other.root.left) and \
                       BST(self.root.right) == BST(other.root.right)
        else:
            return False

    def __ne__(self, other: object) -> bool:
        return not (self == other)
