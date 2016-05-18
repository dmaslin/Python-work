from Graph import Graph
from Graph import Tree
f = input("Enter a filename: ")

fin = open(f, "r")
l = fin.readline()
l = list(l)
l = eval(l[0])
v = []
for i in range(l):
    v.append(fin.readline().split(" "))

for row in range(len(v)):
    for column in range(len(v[row])):
        v[row][column] = eval(v[row][column])
counter = 0
vertex = []
for i in range(len(v)):
    vertex.append(str(v[i][0]))
edges = []
for i in range(l):
    for j in range(1, len(v[i])):
        edges.append([])
        edges[counter].append(i)
        edges[counter].append(v[i][j])
        counter += 1

g = Graph(vertex, edges)
tree = g.dfs(0)
print("The number of vertricies is: " + str(l))
g.printEdges()
if tree.getNumberOfVerticesFound() == l:
    print("They are connected")
else:
    print("They are not connected")


