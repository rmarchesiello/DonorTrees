# Your solution for the donor problem here
from bst_tree import BST
from bst_node import BSTNode
import sys

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        textFile = f.read()

    firstBSTNode = BSTNode(10)
    print(firstBSTNode.value)

    firstBST = BST()
    firstBST.add_value(10)
    print(firstBST.root.value)
    firstBST.add_value(5)
    print(firstBST.length)
    print(firstBST.root.leftChild.value)
    print(firstBST)
