from tkinter import * # Import tkinter
from Graph import Graph
import networkx as nx
from WeightedGraph23_13 import WeightedGraph

class GraphView(Canvas):
    def __init__(self, graph, container, width = 800, height = 450):
        super().__init__(container, width = width, height = height)
        self.graph = graph
        e = self.WeightedGraph.getEdges()
        self.arrowed = []
        for i in e:
            self.arrowed.append(False)
        self.drawGraph()
    def shortestPath(self, source, target):
        g = nx.MultiGraph()
        nodes = []
        for i in range(self.graph.getSize()):
            nodes.append(i)
        g.add_nodes_from(nodes)

        edges = WeightedGraph.getEdges()

        for i in range(len(edges)):
            g.add_edge(edges[i][0], edges[i][1], weight = edges[i][2])

        path = nx.shortest_path(g, source = source, target = target)

        for i in range(1, len(path)):
            n1 = path[i - 1]
            n2 = path[i]
            for j in range(len(edges)):
                if edges[j][0] == n1 and edges[j][1] == n1:
                    self.arrowed[j] = True
        self.drawGraph()

    def drawGraph(self):
        vertices = self.graph.getVertices()
        edges = WeightedGraph.getEdges()
        
        for i in range(len(edges)):
            x1 = self.graph.getVertex(edges[i][0]).getX()
            y1 = self.graph.getVertex(edges[i][0]).getY()
            x2 = self.graph.getVertex(edges[i][1]).getX()
            y2 = self.graph.getVertex(edges[i][1]).getY()
            if self.arrowed[i] == False:
                self.create_line(x1, y1, x2, y2)
            elif self.arrowed[i] == True:
                self.create_line(x1, y1, x2, y2, fill = "red", arrowed = LAST)
        for i in range(self.graph.getSize()):
            x = vertices[i].getX()
            y = vertices[i].getY()
            name = vertices[i].getName()
          
            # Display a vertex
            self.create_oval(x - 2, y - 2, x + 2, y + 2, 
                 fill = "black") 
            # Display the name
            self.create_text(x, y - 8, text = str(name))
