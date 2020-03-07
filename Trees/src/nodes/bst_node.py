from typing import Generic, Iterable, TypeVar, Optional

T = TypeVar('T')


class BSTNode(Generic[T]):
    """
    Your node should permit at least the following
    node.left: get the left child
    node.right: gert the right child
    """

    def __init__(self, value: T, children: Optional[Iterable["BSTNode[T]"]] = None,
                 parent: Optional["BSTNode[T]"] = None) -> None:
        """
        :param value: The value to store in the node
        :param children: optional children
        :param parent: an optional parent node
        """
        self.value = value
        self.children = [None, None]
        self.leftChild = None
        self.rightChild = None
        self.parent = parent

    def __iter__(self) -> Iterable["BSTNode[T]"]:
        """
        Iterate over the children of this node.
        :return:
        """
        if self.leftChild is not None:
            yield self.leftChild
        if self.rightChild is not None:
            yield self.rightChild

    def getRightChild(self):
        if self.rightChild is None:
            return -1
        else:
            return self.rightChild

    def getLeftChild(self):
        if self.leftChild is None:
            return -1
        else:
            return self.leftChild