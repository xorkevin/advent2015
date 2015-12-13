def parsefloor(floortext):
    xFloor = 0
    for c in floortext:
        if c == '(':
            xFloor += 1
        else:
            xFloor -= 1
    return xFloor

def findPosition(floortext, floornum):
    xFloor = 0
    xPos = 0
    for c in floortext:
        if c == '(':
            xFloor += 1
        else:
            xFloor -= 1
        xPos += 1
        if xFloor == floornum:
            break
    return xPos

f = None
with open('advent1data.txt') as d:
    f = d.read().strip()

print('floor: {0}\nposition: {1}'.format(parsefloor(f), findPosition(f, -1)))
