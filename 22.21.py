from tkinter import *
from Graph import Graph
from Graph import Tree

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

        Label(frame, text = "Starting vertex: ").pack(side = LEFT)
        self.v1 = StringVar()
        Entry(frame, textvariable = self.v1, width = 3).pack(side = LEFT)
        self.v2 = StringVar()
        self.v3 = StringVar()

        Button(frame, text = "DFS Tree", command = self.dfs).pack(side = LEFT)
        Button(frame, text = "BFS Tree", command = self.bfs).pack(side = LEFT)

        Label(frame, text = "\tStarting vertex").pack(side = LEFT)
        Entry(frame, textvariable = self.v2, width = 3).pack(side = LEFT)
        Label(frame, text ="Ending vertex").pack(side = LEFT)
        Entry(frame, textvariable = self.v3, width = 3).pack(side = LEFT)
        Button(frame, text ="Shortest Path", command = self.spath).pack(side = LEFT)

        

        

        window.mainloop()

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
                r = []
                r.append(self.edge[len(self.edge) - 1][1])
                r.append(self.edge[len(self.edge) - 1][0])
                self.edge.append(r)
                self.generate()

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
        
                
        

    def dfs(self):
        self.lines = True
        graph = Graph(self.point, self.edge)
        dfs = graph.dfs(eval(self.v1.get()))
        order = dfs.getSearchOrders()
        for i in range(1, len(order)):
            for j in range(len(self.edge)):
                parent = dfs.getParent(i)
                self.canvas.create_line(self.node[parent][0], self.node[parent][1], self.node[order[i]][0], self.node[order[i]][1], arrow = LAST, fill = "red")
        self.generate()

    def bfs(self):
        self.lines = True
        graph = Graph(self.point, self.edge)
        bfs = graph.bfs(eval(self.v1.get()))
        order = bfs.getSearchOrders()
        for i in range( 1, len(order)):
            parent = bfs.getParent(i)
            self.canvas.create_line(self.node[parent][0], self.node[parent][1], self.node[order[i]][0], self.node[order[i]][1], arrow = LAST, fill = "red")

    def spath(self):
        graph = Graph(self.point, self.edge)
        bfs = graph.bfs(eval(self.v2.get()))
        path = bfs.getPath(eval(self.v3.get()))
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
        if self.lines == True:
            self.lines = False
        for i in range(len(self.node)):
            self.points.append(self.canvas.create_oval(self.node[i][0] - self.radius, self.node[i][1] - self.radius, self.node[i][0] + self.radius, self.node[i][1] + self.radius, fill = "white",  tags = str(i)))
            self.canvas.create_text(self.node[i][0], self.node[i][1], text = str(i), tags = str(i))
            
            









        
graphGUI()
