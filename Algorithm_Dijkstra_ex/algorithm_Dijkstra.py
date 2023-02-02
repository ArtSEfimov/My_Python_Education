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
g.connect_node(Node('a'), Node('d'), 2)

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

start_node.value = 0


class MyQueue:
    def __init__(self):
        self.queue = list()

    def add_item(self, item):
        self.queue.append(item)
        self.queue.sort(key=lambda x: x.value)

    def pop_item(self):
        if self.queue:
            return self.queue.pop(0)
        return False

    def __iter__(self):
        for elem in self.queue:
            yield elem

    def __bool__(self):
        return bool(self.queue)

    def __str__(self):
        return str(self.queue)


my_queue = MyQueue()

my_queue.add_item(start_node)

while my_queue:
    current_node = my_queue.pop_item()
    for node, distance in my_graph[current_node].items():
        tmp_value = current_node.value + distance
        if tmp_value < node.value:
            node.value = tmp_value
            if node not in my_queue:
                my_queue.add_item(node)
    print(my_queue)

finish_node = Node('g')
path = ''

PATHS = []


def get_path(node, path):
    path += node.name
    if node.name == 'a':
        PATHS.append(path)
        return
    for tmp_node, tmp_distance in my_graph[node].items():
        if node.value - tmp_distance == tmp_node.value:
            get_path(tmp_node, path)


get_path(finish_node, path)
print(
    PATHS
)
