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
    firstBST.add_value(30)
    firstBST.add_value(15)
    firstBST.add_value(13)
    firstBST.add_value(40)
    firstBST.add_value(39)    
    firstBST.add_value(31)
    
    print(firstBST.get_max_node().value)