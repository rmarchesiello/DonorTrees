# Your solution for the donor problem here
from Trees.src.trees.bst_tree import BST
from Trees.src.nodes.bst_node import BSTNode
from Trees.src.donor_prog.donor import Donor
import sys, math

if __name__ == "__main__":
    #tree = BST()
    #tree.add_value(100)
    #tree.add_value(80)
    #tree.add_value(200)
    #tree.add_value(90)
    #tree.add_value(70)

    #root = BSTNode(100)
    #root.leftChild = BSTNode(80)
    #root.rightChild = BSTNode(200)
    #root.leftChild.leftChild = BSTNode(70)
    #root.leftChild.rightChild = BSTNode(90)

    ## check if the list of their nodes' values are the same:
    #treeNodes = [tree.root.value, tree.root.leftChild.value, tree.root.leftChild.leftChild.value,
    #                tree.root.leftChild.rightChild.value,
    #                tree.root.rightChild.value]
    #rootNodes = [root.value, root.leftChild.value, root.leftChild.leftChild.value,
    #                root.leftChild.rightChild.value, root.rightChild.value]
    #cmp_tree = BST(root)

    #print(cmp_tree.height)

    #print('p')


    def findDonorDonation(donorNode : BSTNode(Donor)):
        return donorNode.donation
    
    donorsTree = BST(key = findDonorDonation)

    listOfDonors = []
    with open(sys.argv[1]) as f:
        textFile = f.readlines()
        
        for donor in textFile:
            donorID, donationAmount = donor.split(' : ')
            donorID = int(donorID)
            donationAmount = int(donationAmount)
            donorsTree.add_value(Donor(donorID, donationAmount))

    donorsTree.storeInorder(donorsTree.root)

    if sys.argv[2] == "all":
        donorsTree.printInorder(donorsTree.root)
    elif sys.argv[2] == "rich":
        print(donorsTree.inorderList[-1])
    elif sys.argv[2] == "cheap":
        print(donorsTree.inorderList[0])
    elif sys.argv[2] == "who":
        if sys.argv[3][0] == '+':
            amount = int(sys.argv[3][1:])
            counter = 0
            for i in donorsTree.inorderList:
                if i.donation >= amount:
                    print(i)
                    counter += 1
                    break
            if counter == 0:
                print("No Match")
        elif sys.argv[3][0] == '-':
            amount = int(sys.argv[3][1:])
            if amount > donorsTree.inorderList[-1].donation:
                print(donorsTree.inorderList[-1])
            elif amount < donorsTree.inorderList[0].donation:
                print("No Match")
            else:
                curDonorLessThanAmount = donorsTree.inorderList[0]
                for i in donorsTree.inorderList:
                    if i.donation < amount and i.donation >= curDonorLessThanAmount.donation:
                        curDonorLessThanAmount = i
                        continue
                    print(curDonorLessThanAmount)
                    break
        else:
            amount = int(sys.argv[3])
            flag = False
            for i in donorsTree.inorderList:
                if amount == i.donation:
                    print(i)
                    flag = True
            if not flag:
                print("No Match")
    else:
        print("No Match")
    