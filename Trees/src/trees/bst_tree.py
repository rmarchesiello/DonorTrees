from typing import Optional, Callable, TypeVar, Generic

from Trees.src.errors import MissingValueError, EmptyTreeError
from Trees.src.nodes.bst_node import BSTNode

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

    @property
    def height(self) -> int:
        """
        Compute the height of the tree. If the tree is empty its height is -1
        :return:
        """
        if self.length == 0:
            return -1
        else:  # I think the height of a BST is log base 2 N; but ill check on that
            pass

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
        curNode = self.root
        # base case- tree is empty so create a node and make it the root
        if self.root is None:
            self.root = BSTNode(value)
            self.length = self.length + 1

        elif self.key(value) < self.key(curNode.value):  # I think we have to call key on this??
            if curNode.getLeftChild() == -1:  # in other words, if curNode doesn't have a left child..
                curNode.leftChild = BSTNode(value, parent=curNode)
                self.length = self.length + 1
            else:
                self.add_value(value,
                               curNode.leftChild)  # recursive call to continue to find the correct spot for entry

        else:  # value > curNode.rightChild:
            if curNode.getRightChild() == -1:
                curNode.rightChild = BSTNode(value, parent=curNode)
                self.length = self.length + 1
            else:
                self.add_value(value, curNode.rightChild)

        # elif value < curNode.value: #go down left side
        #     curNode.leftChild = self.add_value(value, curNode.leftChild) #recursive call
        #     curNode.leftChild.parent = curNode
        #
        # else: # go down right side
        #     curNode.rightChild = self.add_value(value, curNode.rightChild)
        #     curNode.rightChild.parent = curNode

    def get_node(self, value: K) -> BSTNode[T]:
        """
        Get the node with the specified value
        :param value:
        :raises MissingValueError if there is no node with the specified value
        :return:
        """
        ...

    def get_max_node(self) -> BSTNode[T]:
        """
        Return the node with the largest value in the BST
        :return:
        :raises EmptyTreeError if the tree is empty
        """
        ...

    def get_min_node(self) -> BSTNode[T]:
        """
        Return the node with the smallest value in the BST
        :return:
        """
        ...

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
        ...

    def __eq__(self, other: object) -> bool:
        if self is other:
            return True
        elif isinstance(other, BST):
            if len(self) == 0 and len(other) == 0:
                return True
            else:
                return len(self) == len(other) and self.root.value == other.root.value and \
                       all((BST(c1) == BST(c2) for c1, c2 in zip(self.root, other.root)))
        else:
            return False

    def __ne__(self, other: object) -> bool:
        return not (self == other)
