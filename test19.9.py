from binarytree19_9 import BinaryTree
from stack import Stack


tree = BinaryTree()
tree.insert("George")
tree.insert("Michael")
tree.insert("Tom")
tree.insert("Adam")
tree.insert("Jones")
tree.insert("Peter")
tree.insert("Daniel")

# Traverse tree
print("Inorder (sorted): ", end = "")
x = tree.inorder()
z = []
for i in range(x.getSize()):
    z.append(x.pop())
z.reverse()
for i in range(len(z)):
    print(z[i], end = " ")
print("\nPostorder: ", end = "")
a = tree.postorder()
b = []
for i in range(a.getSize()):
    b.append(a.pop())
b.reverse()
for i in b:
    print(i, end = " ")
print("\nPreorder: ", end = "")
tree.preorder()
print("\nBreadth-First: ", end = "")
tree.breadthFirstTraversal()
print("\nThe number of nodes is " + str(tree.getSize()), end = "")
print("\nThe height is "+str(tree.height()), end = "")
print("\nThe number of non-leaf nodes is "+ str(tree.nonLeafNodes()))
# Search for an element
print("Is Peter in the tree? " + str(tree.search("Peter")))

# Get a path from the root to Peter
print("A path from the root to Peter is: ");
path = tree.path("Peter")
for node in path:
    print(node.element, end = " ")

numbers = [2, 4, 3, 1, 8, 5, 6, 7]
intTree = BinaryTree()
for e in numbers:
    intTree.insert(e)
    
print("\nInorder (sorted): ", end = "")
y = intTree.inorder()
z = []
for i in range(y.getSize()):
    z.append(y.pop())
z.reverse()
for i in range(len(z)):
    print(z[i], end = " ")
