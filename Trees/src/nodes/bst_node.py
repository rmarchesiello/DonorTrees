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
        self.left = None
        self.right = None
        self.parent = parent
        self.lengthFollowing = 0
                             
    def __iter__(self) -> Iterable["BSTNode[T]"]:
        """
        Iterate over the children of this node.
        :return:
        """
        if self.left is not None:
            yield self.left
        if self.right is not None:
            yield self.right

    def findLengthOfNode(self, root):
        if root:
            self.findLengthOfNode(root.left)
            self.findLengthOfNode(root.right)
            self.lengthFollowing += 1

    def getLenFollowingNode(self):
        self.findLengthOfNode(root = self)
        return self.lengthFollowing

    def getright(self):
        if self.right is None:
            return -1
        else:
            return self.right

    def getleft(self):
        if self.left is None:
            return -1
        else:
            return self.left

    def numChildren(self):
        if self.left == None and self.right == None:
            return 0
        elif self.left != None and self.right == None: #left child only
            return 1
        elif self.left == None and self.right != None: #right child only
            return 1
        else:
            return 2