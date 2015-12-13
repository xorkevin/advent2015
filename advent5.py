def findVowels(text):
    v = 'aeiou'
    count = 0
    for i in v:
        count += text.count(i)
    if count > 2:
        return True

def findDouble(text):
    ab = 'abcdefghijklmnopqrstuvwxyz'
    for i in ab:
        if i+i in text:
            return True

def findExceptions(text):
    ex = [
        'ab',
        'cd',
        'pq',
        'xy',
        ]
    for i in ex:
        if i in text:
            return True

def findDoubleDouble(text):
    for i in range(1, len(text)):
        if text.count(text[i-1:i+1]) > 1:
            return True

def findTriple(text):
    for i in range(2, len(text)):
        a, b, c = text[i-2:i+1]
        if a == c:
            return True

def findNiceStrings(stringList):
    count = 0

    for i in stringList:
        if findVowels(i) and findDouble(i) and not findExceptions(i):
            count += 1

    return count

def findOtherNiceStrings(stringList):
    count = 0

    for i in stringList:
        if findDoubleDouble(i) and findTriple(i):
            count += 1

    return count

f = None
with open('advent5data.txt') as d:
    f = d.read().strip().split('\n')

print('nice strings: {0}\nother nice strings: {1}'.format(findNiceStrings(f), findOtherNiceStrings(f)))
