import networkx as nx

def getMaxSubgraph(edge, key):#edge will need to be a multi-dimensional list where each element will be the edges such as [(node1, node2)] 
    nodes = []
    e = []#list of tuples for nx.Graph
    for a in edge:
        e.append(tuple(a))
    #get nodes used in graph
    for j in range(len(edge)):
        if edge[j][0] not in nodes:
            nodes.append(edge[j][0])
    #create graph
    g = nx.MultiGraph()
    g.add_edges_from(e)
    lst = []
    for i in nodes:
        if g.degree(i) >= key:
            lst.append(i)
    subgraph = []
    for i in range(1, len(lst)):
        if g.has_edge(lst[i-1], lst[i]):
            if lst[i -1] not in subgraph:
                subgraph.append(lst[i - 1])
            if lst[i] not in subgraph:
                subgraph.append(lst[i])
    if len(subgraph) == 0:
        print(None)
    else:
        print(subgraph)


f = input("Enter a filename: ")
k = eval(input("Enter the key for the subgraph: "))

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
getMaxSubgraph(edges, k)

