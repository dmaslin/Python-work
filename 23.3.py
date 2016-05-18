import networkx as nx
#while this can be done using the graph class done last chapter, i find this works easier
#as this uses the smallest number of edges not acutal weight, i will return the weight of the path as well as the path
def shortestPath(vertex, edges, start, end): #edges must be in the format [[vertex 1, vertex 2, weight], ...]
    g = nx.MultiGraph()
    g.add_nodes_from(vertex)
    for i in range(len(edge)):
        a = edge[i][0]
        b = edge[i][1]

        g.add_edge(a, b)
    x = nx.shortest_path(g, source = start, target = end)
    wht = 0
    for i in range(1, len(x)):
        for j in range(len(edges)):
            if x[i - 1] == edges[j][0] and x[i] == edges[j][1]:
                wht += edges[j][2]
    x.append(wht)
    return x

    
