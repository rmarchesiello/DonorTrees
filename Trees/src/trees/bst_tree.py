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
        if self.root != None:
            self.length = self.root.getLenFollowingNode()
        self.inorderList = []
        self.universalCounter = 0

    @property
    def height(self) -> int:
        """
        Compute the height of the tree. If the tree is empty its height is -1
        :return:
        """
        if self.root is None:
            return -1
        else:
            x = self._height(curNode = self.root)
            if x == 0:
                return 0
            else:
                return x

    def _height(self, curNode):
        if curNode is None or (curNode.left == None and curNode.right == None):
            return 0
        else:
            return 1 + max(self._height(curNode.left), self._height(curNode.right))

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
            if curNode.getright() == -1:
                curNode.right = BSTNode(value, parent = curNode)
                self.length += 1
            else:
                newNode = curNode.right
                self.add_value(value, newNode)
        elif self.key(value) < self.key(curNode.value):  # I think we have to call key on this??
            if curNode.getleft() == -1:  # in other words, if curNode doesn't have a left child..
                curNode.left = BSTNode(value, parent=curNode)
                self.length = self.length + 1
            else:
                newNode = curNode.left
                self.add_value(value, newNode)  # recursive call to continue to find the correct spot for entry

        else:  # self.key(value) > self.key(curNode.right):
            if curNode.getright() == -1:
                curNode.right = BSTNode(value, parent=curNode)
                self.length = self.length + 1
            else:
                self.add_value(value, curNode.right)

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
                return self.get_node(value, curNode.left)
            elif value > self.key(curNode.value):
                return self.get_node(value, curNode.right)

            else:
                raise RecursionError
                return None

        except RecursionError as e:
            raise MissingValueError
            return None

    def get_max_node(self) -> BSTNode[T]:
        """
        Return the node with the largest value in the BST
        :return:
        :raises EmptyTreeError if the tree is empty
        """
        curNode = self.root
        while curNode.getright() != -1:
            curNode = curNode.right
        return curNode

    def get_min_node(self) -> BSTNode[T]:
        """
        Return the node with the smallest value in the BST
        :return:
        """
        curNode = self.root
        while curNode.getleft() != -1:
            curNode = curNode.left
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
            if nodeToRemove == None:
                raise MissingValueError
            else:
                if nodeToRemove.numChildren() == 0:
                    del nodeToRemove
                    self.length -= 1

                elif nodeToRemove.numChildren() == 1:
                    if nodeToRemove.getright() != -1:
                        temp = nodeToRemove.right
                        curParent = nodeToRemove.parent
                        if nodeToRemove is self.root:
                            self.root = nodeToRemove.right
                            del nodeToRemove
                        elif nodeToRemove is nodeToRemove.parent.left:
                            del nodeToRemove
                            curParent.left = temp
                        elif nodeToRemove is nodeToRemove.parent.right:
                            del nodeToRemove
                            curParent.right = temp
                        self.length -= 1
                    else:
                        temp = nodeToRemove.left
                        curParent = nodeToRemove.parent
                        if nodeToRemove is self.root:
                            self.root = nodeToRemove.left
                            del nodeToRemove
                        elif nodeToRemove is nodeToRemove.parent.right:
                            del nodeToRemove
                            curParent.right = temp
                        elif nodeToRemove is nodeToRemove.parent.left:
                            del nodeToRemove
                            curParent.left = temp
                        self.length -= 1
                elif nodeToRemove.numChildren() == 2:
                    curNode = nodeToRemove.right
                    while curNode.getleft() != -1:
                        curNode = curNode.left
                    nodeToRemove.value = curNode.value
                    del curNode
                    self.length -= 1
        except MissingValueError as e:
            Exception(e)

    def printPreorder(self, root):
        if root:
            print(root.value)
            self.printPreorder(root.left)
            self.printPreorder(root.right)

    def printInorder(self, root, reverse = False):
        if reverse == False:
            if root:
                self.printInorder(root.left)
                print(root.value)
                self.printInorder(root.right)
        else:
            if root:
                self.printInorder(root.right)
                print(root.value)
                self.printInorder(root.left)

    def storeInorder(self, root):
        if root:
            self.storeInorder(root.left)
            self.inorderList.append(root.value)
            self.storeInorder(root.right)

    def printPostorder(self, root):
        if root:
            self.printPostorder(root.left)
            self.printPostorder(root.right)
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
