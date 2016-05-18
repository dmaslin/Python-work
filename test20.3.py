from AVLTree20_3 import AVLTree

tree = AVLTree()

for i in range(1, 101):
    tree.insert(i)
x = tree.getLeafNodes()
for i in range(len(x)):
 path = [x.element for x in tree.getPath(x[i])]
 print(path,"\n---------------------")
