# Your solution for the donor problem here
from bst_tree import BST
from bst_node import BSTNode


if __name__ == "__main__":
    firstBSTNode = BSTNode(10)
    print(firstBSTNode.value)

    firstBST = BST()
    firstBST.add_value(10)
    print(firstBST.root.value)


