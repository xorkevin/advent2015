def parseDiffDecode(string):
    k = 0
    a = len(string)
    text = string[1:len(string)-1]
    if len(text) < 1:
        return a - k
    text = list(text)
    while len(text)>0:
        b = text.pop(0)
        if b == '\\':
            b = text.pop(0)
            if b == 'x':
                text.pop(0)
                text.pop(0)
        k += 1
    return a - k

def parseDiffEncode(string):
    k = 2
    a = len(string)
    text = list(string)
    while len(text)>0:
        b = text.pop(0)
        if b == '\\' or b == '\"':
            k += 1
        k += 1
    return k - a

def countDiff(strings, encode = False):
    k = 0
    j = 0
    if encode:
        action = parseDiffEncode
    else:
        action = parseDiffDecode

    for i in strings:
        k += action(i)
        j += 1
        print('line {0}'.format(j), flush=True)
    return k

f = None
with open('advent8data.txt') as d:
    f = d.read().strip().split('\n')

print('diff in string length: {0}\ndiff in encoded string length: {1}'.format(countDiff(f), countDiff(f, True)))
