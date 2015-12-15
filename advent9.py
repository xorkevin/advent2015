from itertools import permutations

class Node:
    def __init__(self, key):
        '''paths is a dictionary that has key - node and value - cost of path to node'''
        self._key = key
        self._paths = dict()

    def connect(self, other, cost):
        '''other should be a key of another node; cost is to that node from this'''
        self._paths[other] = cost

    def getCost(self, other):
        return self._paths[other]


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

    def getCost(self, path):
        '''path should be a list of node keys'''
        if len(path) < 2:
            return 0

        cost = 0
        for i in range(1, len(path)):
            cost += self.getNode(path[i-1]).getCost(path[i])

        return cost


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
    longest = 0
    longestPath = None
    shortest = sys.maxsize
    shortestPath = None

    for i in permutations(list(graph._nodes)):
        pathCost = graph.getCost(i)
        if longest < pathCost:
            longest = pathCost
            longestPath = i
        if shortest > pathCost:
            shortest = pathCost
            shortestPath = i

    return {'longest': {'cost': longest, 'path': longestPath}, 'shortest': {'cost': shortest, 'path': shortestPath}}

def parseInstruct(instructs, network):
    for i in instructs:
        pass
        #need to check for uniqueness of nodes, do not overwrite same node

f = None
with open('advent9data.txt') as d:
    f = d.read().strip().split('\n')

net = Network()
