import networkx as nx

f = input("Enter a filename: ").strip()
num1, num2 = eval(input("Enter two nodes: "))



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

g = nx.MultiGraph()
g.add_nodes_from(nodes)
for i in range(len(edges)):
    g.add_edge(edges[i][0], edges[i][1], weight = edges[i][2])
for i in range(num):
    print("Vertex "+str(i)+":", end = " ")
    for j in range(len(edges)):
        if edges[j][0] == i:
            print(edges[j], end = " ")
    print("")
print("The shortest path of "+ str(num1) + " and "+str(num2)+" is: ", end = "")
path = nx.shortest_path(g, source = num1, target = num2)
print(path)





        
        
