from bst_node import BSTNode
from bst_tree import BST

if __name__ == "__main__":
    tree = BST()
    tree.add_value(100)
    tree.add_value(10)
    root = BSTNode(100)
    root.leftChild = BSTNode(10)

    if isinstance(root, BSTNode):
        print("yes lol ")

    rootBST = BST(root)  # right here is the problem - we creat a BST out of a BSTNode, but in creating a BST
    # that value, which is a BSTNode, is instantiated as a BSTNode again inside of BST

    print(tree.root)
    print(rootBST.root)
    print()
    print(tree.root.value)  # these two lines right here highlight the problem currently
    print(rootBST.root.value)

    if tree.root.value == rootBST.root.value:
        print("their values are the same")

    print()

    print(tree.root.leftChild.value)
    print(rootBST.root.leftChild.value)  # this guy doesnt appear to get a left child - why? - line

    if tree.root.leftChild.value == rootBST.root.leftChild.value:
        print("Their left children are the same value: ")
        print(tree.root.leftChild.value)
        print(rootBST.root.leftChild.value)

    tree2BST = BST(tree.root.value)
    root2BST = BST(tree.root.value)
    print("the type of the two objects:")
    print(type(tree2BST))
    print(type(root2BST))

    print()

    print("the values of the two objects' roots:")
    print(tree2BST.root.value)
    print(root2BST.root.value)

    tree.__eq__(root2BST)
