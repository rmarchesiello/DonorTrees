# Your solution for the donor problem here
from Trees.src.trees.bst_tree import BST
from Trees.src.nodes.bst_node import BSTNode
from Trees.src.donor_prog.donor import Donor
import sys, math

if __name__ == "__main__":
    tree = BST()
    # tree.add_value(100)
    # tree.add_value(80)
    # tree.add_value(200)
    # tree.add_value(90)
    # tree.add_value(70)
    #
    # root = BSTNode(100)
    # root.left = BSTNode(80)
    # root.right = BSTNode(200)
    # root.left.left = BSTNode(70)
    # root.left.right = BSTNode(90)
    #
    # print(tree.__len__())
    # tree.remove_value(80)
    # tree.printPreorder(tree.root)
    # print(tree.__len__())
    # print()
    # tree.remove_value(100)
    # tree.printPreorder(tree.root)
    # print(tree.__len__())

    tree.add_value(200)
    tree.add_value(100)
    tree.add_value(300)
    tree.add_value(50)
    tree.add_value(110)
    tree.add_value(250)
    tree.add_value(500)
    tree.add_value(25)
    tree.add_value(75)
    tree.add_value(105)
    tree.add_value(150)
    tree.add_value(225)
    tree.add_value(275)
    print("tree printed: ")
    tree.printPreorder(root=tree.root)
    print(f"length of the tree: {tree.__len__()}")
    print()
    print()

    tree.remove_value(300)
    print()
    tree.printPreorder(root=tree.root)
    print(f"length of tree after removal: {tree.__len__()}")

    otherTree = BST()
    otherTree.add_value(200)
    otherTree.add_value(500)
    otherTree.add_value(100)
    otherTree.add_value(50)
    otherTree.add_value(110)
    otherTree.add_value(250)

    otherTree.add_value(25)
    otherTree.add_value(75)
    otherTree.add_value(105)
    otherTree.add_value(150)
    otherTree.add_value(225)
    otherTree.add_value(275)

    otherTree.printPreorder(root=otherTree.root)
    print(f"length of otherTree:{otherTree.__len__()}")

    # print(tree.root.value)
    # print(tree.root.left.value)
    # print(tree.root.left.left.value)
    # print(tree.root.left.right)
    # print(tree.root.right.value)

    # cmp_tree = BST(root)

    # print(cmp_tree.height)

    # print('p')

    # def main():
    #
    #     def findDonorDonation(donorNode: BSTNode(Donor)):
    #         return donorNode.donation
    #
    #     donorsTree = BST(key=findDonorDonation)
    #
    #     listOfDonors = []
    #     with open(sys.argv[1]) as f:
    #         textFile = f.readlines()
    #
    #         for donor in textFile:
    #             donorID, donationAmount = donor.split(' : ')
    #             donorID = int(donorID)
    #             donationAmount = int(donationAmount)
    #             donorsTree.add_value(Donor(donorID, donationAmount))
    #
    #     donorsTree.storeInorder(donorsTree.root)
    #
    #     if sys.argv[2] == "all":
    #         donorsTree.printInorder(donorsTree.root)
    #     elif sys.argv[2] == "rich":
    #         print(donorsTree.inorderList[-1])
    #     elif sys.argv[2] == "cheap":
    #         print(donorsTree.inorderList[0])
    #     elif sys.argv[2] == "who":
    #         if sys.argv[3][0] == '+':
    #             amount = int(sys.argv[3][1:])
    #             counter = 0
    #             for i in donorsTree.inorderList:
    #                 if i.donation >= amount:
    #                     print(i)
    #                     counter += 1
    #                     break
    #             if counter == 0:
    #                 print("No Match")
    #         elif sys.argv[3][0] == '-':
    #             amount = int(sys.argv[3][1:])
    #             if amount > donorsTree.inorderList[-1].donation:
    #                 print(donorsTree.inorderList[-1])
    #             elif amount < donorsTree.inorderList[0].donation:
    #                 print("No Match")
    #             else:
    #                 curDonorLessThanAmount = donorsTree.inorderList[0]
    #                 for i in donorsTree.inorderList:
    #                     if i.donation < amount and i.donation >= curDonorLessThanAmount.donation:
    #                         curDonorLessThanAmount = i
    #                         continue
    #                     print(curDonorLessThanAmount)
    #                     break
    #         else:
    #             amount = int(sys.argv[3])
    #             flag = False
    #             for i in donorsTree.inorderList:
    #                 if amount == i.donation:
    #                     print(i)
    #                     flag = True
    #             if not flag:
    #                 print("No Match")
    #     else:
    #         print("No Match")
    #
    #
    # main()
