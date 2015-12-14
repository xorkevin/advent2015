op = {
    'OR'    : lambda x, y: x|y,
    'AND'   : lambda x, y: x&y,
    'NOT'   : lambda x   : ~x,
    'LSHIFT': lambda x, y: x<<y,
    'RSHIFT': lambda x, y: x>>y,
    'PASS'  : lambda x   : x,
    }

class Node:
    def __init__(self, operator=None, inp=None, val=None, string=None):
        self._val = val
        self._input = inp
        self._operator = operator
        self._string = string

    def getVal(self):
        if self._val is None:
            o = self._operator
            if o == 'NOT' or o == 'PASS':
                x = nodeset[self._input[0]].getVal()
                self._val = op[o](x)
            else:
                x, y = self._input
                try:
                    x = int(x)
                except ValueError:
                    x = nodeset[x].getVal()
                try:
                    y = int(y)
                except ValueError:
                    y = nodeset[y].getVal()
                self._val = op[o](x, y)
        return self._val

    def setVal(self, val):
        self._val = val

    def __str__(self):
        return self._string

    def __repr__(self):
        return self._string

nodeset = {}

def resetNodes():
    global nodeset
    nodeset = {}

resetNodes()


def initNodes(instructs):
    for i in instructs:
        lhs, rhs = i.split(' -> ')
        lhs = lhs.split(' ')

        if len(lhs) < 2:
            k = lhs[0]
            try:
                k = int(k)
                nodeset[rhs] = Node(val=k, string=i)
            except ValueError:
                nodeset[rhs] = Node(operator='PASS', inp=[k], string=i)
        elif lhs[0] == 'NOT':
            nodeset[rhs] = Node(operator='NOT', inp=[lhs[1]], string=i)
        else:
            nodeset[rhs] = Node(operator=lhs[1], inp=[lhs[0], lhs[2]], string=i)


f = None
with open('advent7data.txt') as d:
    f = d.read().strip().split('\n')

# with open('testing.txt') as d:
#     f = d.read().strip().split('\n')

initNodes(f)
aVal = nodeset['a'].getVal()
print('wire a val: {0}'.format(aVal))

resetNodes()
initNodes(f)
nodeset['b'].setVal(aVal)
aVal2 = nodeset['a'].getVal()
print('wire a val with b overide: {0}'.format(aVal2))
