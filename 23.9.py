from WeightedGraph import WeightedGraph

f = input("Enter a filename: ").strip()

fin = open(f)
num = fin.readline()

edges = []
nodes = []

for i in range(num):
    nodes.append(i)

for i in range(num):
    x = fin.readline()
    if " | " in x:
        x = x.split(" | ")
        x1 = x[0]
        x1 = x1.split(", ")
        for a in range(len(x1)):
            x1[a] = eval(x1[a])
        x2 = x[1]
        x2 = x2.split(", ")
        for a in range(len(x2)):
            x2[a] = eval(x2[a])
        edges.append([])
        edges[len(edges) - 1].append(x1)
        edges.append([])
        edges[len(edges) - 1].append(x2)
    else:
        x = x.split(", ")
        for a in range(len(x)):
            x[a] = eval(x[a])
        edges.append([])
        edges[len(edges) - 1].append(x)
fin.close()

g = WeightedGraph(nodes, edges)

mst = g.getMinimumSpanningTree()

wht = mst.getTotalWeight()

for i in range(num):
    print("Vertex "+str(i)+":", end = " ")
    for j in range(len(edges)):
        if edges[j][0] == i:
            print(edges[j], end = " ")
    print("")





        
        
