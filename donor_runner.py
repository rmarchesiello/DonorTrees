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
    firstBST.add_value(12)
    
    print(firstBST.root.value)
    print(firstBST.root.rightChild.value)
    print(firstBST.root.rightChild.rightChild.value)
    firstBST.remove_value(11)
    print(firstBST.root.value)
    print(firstBST.root.rightChild.value)