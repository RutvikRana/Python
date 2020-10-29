"""
Illustration Of Dijkstra's Algorithm.

::::::::::: Created By Rutvik H. Rana:::::::::::::

"""
from Dijkstra import Dijkstra,Node
import tkinter as tk

WIDTH = 700
HEIGHT = 600
RADIUS_NODE = 20
EDGE_WIDTH = 10
COLORS={"node":"black","edge":"grey","start":"blue","end":"green","path":"red"}
is_node_clicked = False
prev_node = None
nodes = []
start_node = None
end_node = None
extra = []

def findPath():
    global extra

    for i in extra:
        canvas.delete(i)

    path = Dijkstra(nodes).findShortestPath(start_node,end_node)
    for i in range(1,len(path)):
        extra.append(canvas.create_line(path[i].coords[0],path[i].coords[1],path[i-1].coords[0],path[i-1].coords[1],width=EDGE_WIDTH,fill=COLORS["path"]))
        canvas.tag_raise(path[i].name)
        canvas.tag_raise(path[i-1].name)

def nodeSE(event,canvas):
    global RADIUS_NODE,start_node,end_node

    node = None
    for i in nodes:
        if i.name == event:
            node = i
            break
    if start_node == None:
        start_node = node
        canvas.itemconfigure(node.name,fill=COLORS["start"])
    elif end_node == None:
        end_node = node
        canvas.itemconfigure(node.name,fill=COLORS["end"])
    else:
        canvas.itemconfigure(start_node.name,fill=COLORS["node"])
        canvas.itemconfigure(end_node.name,fill=COLORS["node"])
        canvas.itemconfigure(node.name,fill=COLORS["start"])
        start_node = node
        end_node = None

def nodeClick(event,canvas):
    global is_node_clicked,prev_node,EDGE_WIDTH,RADIUS_NODE
    index = event
    event = canvas.coords(event)
    event = (event[0]+RADIUS_NODE/2,event[1]+RADIUS_NODE/2)
    is_node_clicked = True
    if(prev_node != None):
        canvas.tag_lower(canvas.create_line(event[0],event[1],prev_node[1],prev_node[2],fill=COLORS["edge"],width=EDGE_WIDTH))

        node1=None
        node2=None
        for i in nodes:
            if i.name == index:
                node1 = i
            if i.name == prev_node[0]:
                node2 = i
        if node2 not in node1.connections:
            node1.connections.append(node2)
        if node1 not in node2.connections:
            node2.connections.append(node1)
        prev_node = None
    else:
        prev_node = (index,event[0],event[1])

def makeNode(event,canvas):
    global RADIUS_NODE,is_node_clicked
    if is_node_clicked:
        is_node_clicked = False
        return None
    r = RADIUS_NODE/2
    x,y = event.x,event.y
    oval = canvas.create_oval((x-r,y-r,x+r,y+r), fill=COLORS["node"],outline="")
    nodes.append(Node(oval,(x,y)))
    canvas.tag_bind(oval,"<Button-1>",lambda e:nodeClick(oval,canvas))
    canvas.tag_bind(oval,"<Button-3>",lambda e:nodeSE(oval,canvas))

def reset():
    global nodes,is_node_clicked,prev_node,start_node,end_node,extra
    canvas.delete("all")
    nodes.clear()
    is_node_clicked = False
    prev_node = None
    start_node = None
    end_node = None
    extra.clear()


mainWindow = tk.Tk()
mainWindow.title("Dijkstra's Algorithm Demo")
canvas = tk.Canvas(mainWindow,height=HEIGHT,width=WIDTH,bg="white")
canvas.bind("<Button-1>",lambda event:makeNode(event,canvas))
canvas.grid(row=0,columnspan=2,column=0,padx=10,pady=10)
button = tk.Button(mainWindow,text="Find",command=findPath)
button.grid(row=1,column=0,padx=10,pady=10,sticky=tk.E)
button2 = tk.Button(mainWindow,text="Clear",command=reset)
button2.grid(row=1,column=1,padx=10,pady=10,sticky=tk.W)
mainWindow.mainloop()