def calcSurfaceArea(l, w, h):
    lw = l*w
    wh = w*h
    lh = l*h
    sm = min(lw, min(wh, lh))
    return (lw + wh + lh)*2 + sm

def calcTotal(dimFile, function):
    cumul = 0
    for l in dimFile:
        l, w, h = l.strip().split('x')
        cumul += function(int(l), int(w), int(h))
    return cumul

def calcRibbon(l, w, h):
    lw = l+w
    wh = w+h
    lh = l+h
    sm = min(lw, min(wh, lh))
    return(l*w*h+sm*2)


f = None
with open('advent2data.txt') as d:
    f = d.read().strip().split('\n')

print('area: {0}\nribbon: {1}'.format(calcTotal(f, calcSurfaceArea), calcTotal(f, calcRibbon)))
