import math


class Node:
    NODES = {}

    def __new__(cls, name, *args, **kwargs):
        obj = object.__new__(cls)
        obj.name = name
        return cls.NODES.setdefault(obj.name, obj)

    def __init__(self, name):
        if name in self.__class__.NODES and hasattr(self, 'value'):
            self.name = self.__class__.NODES.get(name).name
            self.value = self.__class__.NODES.get(name).value
        else:
            self.name = name
            self.value = math.inf

    def __repr__(self):
        return self.name


class Graph:
    def __init__(self):
        self.nodes = {}

    def connect_node(self, node_1, node_2, distance):
        self.nodes.setdefault(node_1, {})[node_2] = distance
        self.nodes.setdefault(node_2, {})[node_1] = distance


g = Graph()

g.connect_node(Node('a'), Node('c'), 1)
g.connect_node(Node('a'), Node('g'), 10)
g.connect_node(Node('a'), Node('d'), 4)

g.connect_node(Node('c'), Node('b'), 1)
g.connect_node(Node('c'), Node('e'), 3)
g.connect_node(Node('c'), Node('d'), 3)

g.connect_node(Node('b'), Node('f'), 2)

g.connect_node(Node('e'), Node('d'), 2)
g.connect_node(Node('e'), Node('f'), 2)
g.connect_node(Node('e'), Node('g'), 1)

g.connect_node(Node('f'), Node('g'), 3)

my_graph = g.nodes
print(
    my_graph
)
start_node = Node('a')

PATHS = {}


def walk(node, path, v):
    path += node.name
    value = v
    for n, v in my_graph[node].items():
        if n.name == 'a':
            path += n.name
            value += v
            PATHS[path] = value
            value -= v
            path = path[:-1]
        else:
            if n.name not in path:
                walk(n, path, value + v)


e = Node('e')
walk(e, '', 0)

print(
    PATHS
)
