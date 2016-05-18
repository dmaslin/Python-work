import networkx as nx
#networkx uses Kruskal for its mst 
def Kruskal(vertex, edge):
    g = nx.MultiGraph()
    g.add_nodes_from(vertex)
    for i in edge:
        x = tuple(i)
        g.add_weighted_edges_from(x)
    T = nx.minimum_spanning_tree(g)
    return T
