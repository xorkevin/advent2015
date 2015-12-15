class Node:
    def __init__(self, key):
        '''paths is a dictionary that has key - node and value - cost of path to node'''
        self._key = key
        self._paths = dict()

    def connect(self, other, cost):
        '''other should be a key of another node; cost is to that node from this'''
        self._paths[other] = cost


class Network:
    def __init__(self):
        self._nodes = set()
        self._nodedict = dict()

    def addNode(self, name):
        '''name should be a key of a node'''
        self._nodes.add(name)
        self._nodedict[name] = Node(name)

    def getNode(self, name):
        return self._nodedict[name]
        

def travelSalesman(graph):
    '''this finds the shortest tour through each node of a network
    christofides's algorithm'''
    pass

def minSpanTree(graph):
    '''this finds the minimum spanning tree of a network
    prim's algorithm'''
    pass

def bruteForceSalesman(graph):
    '''checks all possible permutations'''
    pass
