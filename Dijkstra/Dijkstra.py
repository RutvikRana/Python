"""
Dijkstra's Algorithm is One of most awesome Algorithm used to find shortest path.
GOOGLE even use this in Google Maps.

How To Use?
- Make Nodes.
- Use Dijkstra class findShortestPath method

::::::::::: Created By Rutvik H. Rana:::::::::::::

"""

class Dijkstra:

    def __init__(self, nodes):
        self.nodes = nodes

    def __minNode(self, arr=[], finish=None):
        if (len(arr) == 0):
            return None

        min = None
        for i in arr:
            if i.checked:
                continue
            if min == None:
                min = i
            if i.cost < min.cost:
                min = i
        if min.checked or min.name == finish.name:
            return None

        min.checked = True
        return min

    def findShortestPath(self, a, b):
        import math
        if not isinstance(a, Node) or not isinstance(b, Node):
            print("A and B are not nodes...")
            return None
        self.resetNodes(self.nodes)
        a.cost = 0
        arr = [a]

        while (True):
            min = self.__minNode(arr, b)
            if (min == None):
                break

            for i in min.connections:
                arr.append(i)
                distance = min.cost + math.sqrt((i.coords[0] - min.coords[0]) ** 2 + (i.coords[1] - min.coords[1]) ** 2)
                if (i.cost == -1 or i.cost > distance):
                    i.cost = distance
                    i.parent = min

        arr.clear()
        arr = [b]
        while (arr[-1].name != a.name):
            arr.append(arr[-1].parent)
        return arr

    def resetNodes(self, nodes):
        for i in nodes:
            i.cost = -1
            i.parent = None
            i.checked = False


class Node:
    def __init__(self, name, coords=(0,0)):
        self.name = name
        self.coords = coords
        self.connections = []
        self.cost = -1
        self.parent = None
        self.checked = False

    def __repr__(self):
        # return  str(self.name)+"::"+str([i.name for i in self.connections])
        return str(f"Node({self.name})")
        return str(f"Node({self.name},{self.cost},{self.parent},{self.checked})")

#:::::::::Example::::::::::
if __name__=="__main__":

    nodes = [Node(i,(1*i,1*i*i)) for i in [0,1,2,3,4]]
    nodes[0].connections = [nodes[i] for i in [1,2]]
    nodes[1].connections = [nodes[i] for i in [0,3]]
    nodes[2].connections = [nodes[i] for i in [3,4]]
    nodes[3].connections = [nodes[i] for i in [0,2]]
    nodes[4].connections = [nodes[i] for i in [1,3]]

    print(Dijkstra(nodes).findShortestPath(nodes[0],nodes[4]))