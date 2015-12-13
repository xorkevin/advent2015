import numpy as np

moveKey = {
    '^': (0,1),
    '>': (1,0),
    'v': (0,-1),
    '<': (-1,0),
    }

def parseLocation(directions):
    xp = 0
    yp = 0
    locSet = set([(xp, yp)])

    for move in directions:
        dx, dy = moveKey[move]
        xp += dx
        yp += dy
        locSet.add((xp, yp))

    return len(locSet)

def doubleParseLocation(directions):
    xp = 0
    yp = 0
    xq = 0
    yq = 0
    locSet = set([(xp, yp)])
    first = True

    for move in directions:
        dx, dy = moveKey[move]
        if first:
            first = False
            xp += dx
            yp += dy
            locSet.add((xp, yp))
        else:
            first = True
            xq += dx
            yq += dy
            locSet.add((xq, yq))

    return len(locSet)

f = None
with open('advent3data.txt') as d:
    f = d.read().strip()

print('houses: {0}\ndouble houses: {1}'.format(parseLocation(f), doubleParseLocation(f)))
