# Your solution for the donor problem here
from Trees.src.trees.bst_tree import BST
from Trees.src.nodes.bst_node import BSTNode
import sys

if __name__ == "__main__":
    #with open(sys.argv[1]) as f:
    #    textFile = f.read()

    firstBSTNode = BSTNode(10)
    #print(firstBSTNode.value)

    firstBST = BST()
    firstBST.add_value(10)
    firstBST.add_value(5)
    firstBST.add_value(11)
    firstBST.add_value(1)
    firstBST.add_value(6)
    
    print(firstBST.root.value)
    print(firstBST.root.leftChild.rightChild.value)
    for val in firstBST.root:
        print(val.value)

    print(firstBST.get_node(5))
    print(firstBST.root.leftChild)

