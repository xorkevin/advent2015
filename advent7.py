operation = {
    'OR'    : lambda x, y: x|y,
    'AND'   : lambda x, y: x&y,
    'NOT'   : lambda x, y: ~x,
    'LSHIFT': lambda x, y: x<<y,
    'RSHIFT': lambda x, y: x>>y,
    'PASS'  : lambda x, y: x,
    }

class Node:
    def __init__(self, operator=None, inp=None, val=None, string=None):
        self._val = val
        self._input = inp
        self._operator = operator
        self._string = string

    def getVal(self):
        if self._val is None:
            x, y = self._input
            print(x, y)
            print(nodeset[x], nodeset[y])
            x, y = nodeset[x], nodeset[y]
            self._val = self._operator(x.getVal(), y.getVal())
        return self._val

    def __str__(self):
        return self._string

nodeset = {
    'dummynode': Node(val=0)
    }

def resetNodes():
    global nodeset
    nodeset = {'dummynode': Node(val=0)}

resetNodes()


def initNodes(instructs):
    for i in instructs:
        lhs, rhs = i.split(' -> ')
        lhs = lhs.split(' ')

        if len(lhs) < 2:
            k = lhs[0]
            try:
                k = int(k)
                nodeset[rhs] = Node(val=k)
            except ValueError:
                print(k)
                nodeset[rhs] = Node(operator=operation['PASS'], inp=[k, 'dummynode'])
        elif lhs[0] == 'NOT':
            nodeset[rhs] = Node(operator=operation[lhs[0]], inp=[lhs[1], 'dummynode'])
        else:
            nodeset[rhs] = Node(operator=operation[lhs[1]], inp=[lhs[0], lhs[2]])


f = None
# with open('advent7data.txt') as d:
#     f = d.read().strip().split('\n')

with open('testing.txt') as d:
    f = d.read().strip().split('\n')

initNodes(f)
# print('wire a val: {0}'.format(nodeset['a'].getVal()))

print('wire a val: {0}'.format(nodeset['a'].getVal()))
