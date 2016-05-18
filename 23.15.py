from tkinter import *
from WeightedGraph import WeightedGraph
import networkx as nx

class graphGUI:
    def __init__(self):
        self.node = []
        self.point = []
        self.edge = []
        self.lines = False

        self.radius = 20
        
        window = Tk()
        window.title("Map")

        self.canvas = Canvas(window, height = 400, width = 1000)
        self.canvas.pack()

        self.canvas.create_rectangle(10, 10, 178, 120)
        self.canvas.create_text(20, 20, anchor = W, text = "Instructions")
        self.canvas.create_text(20, 40,anchor = W, text = "Add:\t\tLeft Click")
        self.canvas.create_text(20, 60,anchor = W, text = "Move:\t\tCtrl Drag")
        self.canvas.create_text(20, 80,anchor = W, text = "Connect:\tDrag")
        self.canvas.create_text(20, 100,anchor = W, text = "Remove:\t\tRight Click")

        self.canvas.bind("<Button-1>", self.add)
        self.canvas.bind("<Control-B1-Motion>", self.move)
        self.canvas.bind("<ButtonRelease-1>", self.end)
        self.canvas.bind("<Button-3>", self.remove)
        self.canvas.focus_set()



        frame = Frame(window)
        frame.pack()

        Button(frame, text = "Show MST", command = self.mst).pack(side = LEFT)
        Label(frame, text = "Source vertex: ").pack(side = LEFT)
        self.v1 = StringVar()
        Entry(frame, textvariable = self.v1, width = 3).pack(side = LEFT)
        Button(frame, text = "Show All SP From This Source", command = self.spFromSource).pack(side = LEFT)
        self.v2 = StringVar()
        self.v3 = StringVar()

        Label(frame, text = "\tStarting vertex").pack(side = LEFT)
        Entry(frame, textvariable = self.v2, width = 3).pack(side = LEFT)
        Label(frame, text ="Ending vertex").pack(side = LEFT)
        Entry(frame, textvariable = self.v3, width = 3).pack(side = LEFT)
        Button(frame, text ="Shortest Path", command = self.spath).pack(side = LEFT)

        

        

        window.mainloop()
    def distance(self, x1, x2, y1, y2):
        d = ((x1 - x2)**2 + (y1-y2)**2 )**.5
        return d

    def add(self, event):
        
        if len(self.node) == 0:
            self.node.append([])
            self.node[len(self.node) - 1].append(event.x)
            self.node[len(self.node) - 1].append(event.y)
            self.point.append(0)
            self.generate()
        else:
            t = self.canvas.find_closest(event.x, event.y)
            t = self.canvas.gettags(t)
            t = list(t)
            t = t[0]
            if ((event.x - self.node[int(t)][0])**2 + (event.y - self.node[int(t)][1])**2 )**.5 > 20:
                self.node.append([])
                self.node[len(self.node) - 1].append(event.x)
                self.node[len(self.node) - 1].append(event.y)
                self.point.append(self.point[len(self.point) - 1] + 1)
                self.generate()
            elif ((event.x - self.node[int(t)][0])**2 + (event.y - self.node[int(t)][1])**2 )**.5 < 20:
                self.edge.append([])
                self.edge[len(self.edge) - 1].append(eval(t))

    def move(self, event):
        t = self.canvas.find_closest(event.x, event.y)
        xoffset = event.x - self.node[int(t)][0]
        yoffset = event.y - self.node[int(t)][1]

        self.canvas.move(tag, xoffset, yoffset)
        self.canvas.update()
    def end(self, event):
        if len(self.edge) > 0:
            if len(self.edge[len(self.edge) - 1]) == 1:
                t = self.canvas.find_closest(event.x, event.y)
                t = self.canvas.gettags(t)
                t = list(t)
                t = t[0]
                self.edge[len(self.edge) - 1].append(eval(t))
                wht = self.getWht()
                self.edge[len(self.edge) - 1].append(wht)
                x = self.edge[len(self.edge) - 1]
                a = x[0]
                b = x[1]
                x[0] = b
                x[1] = a
                self.edge.append(x)
                self.generate()

    def getWht(self):
        x1 = self.node[self.edge[len(self.edge) - 1][0]][0]
        y1 = self.node[self.edge[len(self.edge) - 1][0]][1]
        x2 = self.node[self.edge[len(self.edge) - 1][1]][0]
        y2 = self.node[self.edge[len(self.edge) - 1][1]][1]

        wht = self.distance(x1, y1, x2, y2)
        return wht
    def remove(self, event):
        t = self.canvas.find_closest(event.x, event.y)
        t = self.canvas.gettags(t)
        t = list(t)
        t = t[0]
        self.node.pop(eval(t))
        for i in range(len(self.edge)):
            if eval(t) in self.edge[i]:
                self.edge.pop(i)
        self.generate()
        
                
        

    def mst(self):
        self.lines = True
        g = nx.MultiGraph()
        n = []
        for i in range(len(self.node)):
            n.append(i)
        g.add_nodes_from(n)
        for i in range(len(self.edge)):
            g.add_edge(self.edge[i][0], self.edge[i][1], weight = self.edge[i][2])
        t = nx.minimum_spanning_tree(g)
        x = list(t.edges())
        for i in range(len(x)):
            x[i] = list(x[i])
        
        for i in range(1, len(x)):
            self.canvas.create_line(self.node[x[i - 1][0]][0], self.node[x[i - 1][0]][1], self.node[x[i][1]][0], self.node[x[i][1]][1], arrow = LAST, fill = "red")
        self.generate()

    def spFromSource(self):
        self.lines = True
        g = nx.MultiGraph()
        n = []
        for i in range(len(self.node)):
            n.append(i)
        g.add_nodes_from(n)
        for i in range(len(self.edge)):
            g.add_edge(self.edge[i][0], self.edge[i][1], weight = self.edge[i][2])
        p = nx.shortest_path(g, source = eval(self.v1.get()))
        for j in range(len(p)):
            for i in range(1, len(p[j])):
                self.canvas.create_line(self.node[p[j][i - 1]][0], self.node[p[j][i - 1]][1], self.node[p[j][i]][0], self.node[p[j][i]][1], fill = "red")
        self.generate()

    def spath(self):
        g = nx.MultiGraph()
        n = []
        for i in range(len(self.node)):
            n.append(i)
        g.add_nodes_from(n)

        for i in range(len(self.edge)):
            g.add_edge(self.edge[i][0], self.edge[i][1], weight = self.edge[i][2])
        
        path = nx.shortest_path(g, source = eval(self.v2.get()), target = eval(self.v3.get()))
        for i in range(1, len(path)):
            self.canvas.create_line(self.node[path[i - 1]][0], self.node[path[i - 1]][1], self.node[path[i]][0], self.node[path[i]][1], arrow = FIRST, fill = "red")
        


    def generate(self):
        self.points = []
        if self.lines == False:
            self.canvas.delete(ALL)
            self.canvas.create_rectangle(10, 10, 178, 120)
            self.canvas.create_text(20, 20, anchor = W, text = "Instructions")
            self.canvas.create_text(20, 40,anchor = W, text = "Add:\t\tLeft Click")
            self.canvas.create_text(20, 60,anchor = W, text = "Move:\t\tCtrl Drag")
            self.canvas.create_text(20, 80,anchor = W, text = "Connect:\tDrag")
            self.canvas.create_text(20, 100,anchor = W, text = "Remove:\t\tRight Click")
            for j in range(len(self.edge)):
                self.canvas.create_line(self.node[self.edge[j][0]][0], self.node[self.edge[j][0]][1], self.node[self.edge[j][1]][0], self.node[self.edge[j][1]][1])
                x1 = (self.node[self.edge[j][0]][0] + self.node[self.edge[j][1]][0])/ 2
                y1 = (self.node[self.edge[j][0]][1] + self.node[self.edge[j][1]][1])/ 2
                x1 += 10
                y1 += 10
                self.canvas.create_text(x1, y1, text = format(self.edge[j][2], ".0f"))
        if self.lines == True:
            self.lines = False
        for i in range(len(self.node)):
            self.points.append(self.canvas.create_oval(self.node[i][0] - self.radius, self.node[i][1] - self.radius, self.node[i][0] + self.radius, self.node[i][1] + self.radius, fill = "white",  tags = str(i)))
            self.canvas.create_text(self.node[i][0], self.node[i][1], text = str(i), tags = str(i))
            
            









        
graphGUI()
