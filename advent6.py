import numpy as np

grid = None
def resetGrid():
    global grid
    grid = np.zeros((1000, 1000), dtype=np.int)

resetGrid()

def turnOn(val):
    return 1

def turnOff(val):
    return 0

def toggle(val):
    return (val+1)%2

move = {
    'turn on' : turnOn,
    'turn off': turnOff,
    'toggle'  : toggle,
    }

def nTurnOn(val):
    return val+1

def nTurnOff(val):
    return max(0, val-1)

def nToggle(val):
    return val+2

nMove = {
    'turn on' : nTurnOn,
    'turn off': nTurnOff,
    'toggle' : nToggle,
    }

def turn(action, start, finish):
    xi, yi = start
    xf, yf = finish
    for i in range(yi, yf+1):
        for j in range(xi, xf+1):
            grid[i,j] = action(grid[i,j])

def parseInstructSet(instructs, nord):
    if nord == True:
        moveset = nMove
    else:
        moveset = move

    k = 0

    for i in instructs:
        instruct = i.split(' ')
        act = instruct.pop(0)
        if act == 'turn':
            act += ' ' + instruct.pop(0)
        action = moveset[act]
        start = map(int, instruct.pop(0).split(','))
        finish = map(int, instruct.pop().split(','))

        turn(action, start, finish)
        k += 1
        print('instruct: {0}'.format(k), flush=True)

def countLights(instructs, nord=False):
    resetGrid()
    parseInstructSet(instructs, nord)
    if nord:
        return np.sum(grid)
    return len(grid[grid==1])

f = None

with open('advent6data.txt') as d:
    f = d.read().strip().split('\n')

print('lights on: {0}\nnord lights on: {1}'.format(countLights(f), countLights(f, nord=True)))
