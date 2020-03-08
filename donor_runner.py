# Your solution for the donor problem here
from Trees.src.trees.bst_tree import BST
from Trees.src.nodes.bst_node import BSTNode
import sys, math

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        textFile = f.read()

    firstBSTNode = BSTNode(10)
    print(firstBSTNode.value)

    firstBST = BST()
    firstBST.add_value(1142)
    firstBST.add_value(354)
    firstBST.add_value(6020)
    firstBST.add_value(6335)
    firstBST.add_value(2750)
    firstBST.add_value(6941)
    firstBST.add_value(3913)
    firstBST.add_value(8422)
    firstBST.add_value(9608)
    firstBST.add_value(7726)

    
    print("Preorder")
    firstBST.printPreorder(firstBST.root)
    print("Inorder")
    firstBST.printInorder(firstBST.root)
    print("Postorder")
    firstBST.printPostorder(firstBST.root)
    