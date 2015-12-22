from itertools import permutations
import sys


class Table:
    def __init__(self):
        self._people = set()
        self._happyLookup = {}
        self._length = len(self._people)

    def addPerson(self, person):
        '''person is a unique string id'''
        self._people.add(person)
        self._length = len(self._people)

    def addScore(self, a, b, score):
        if a not in self._happyLookup:
            self._happyLookup[a] = {}
        self._happyLookup[a][b] = score

    def getHappiness(self, arr, location):
        person = arr[location]
        n = arr[(location+1) % self._length]
        p = arr[(location-1) % self._length]
        return self._happyLookup[person][n] + self._happyLookup[person][p]

    def getSumHappiness(self, arr):
        k = 0
        for i in range(0, self._length):
            k += self.getHappiness(arr, i)
        return k

    def getMaxHappiness(self):
        maxList = None
        maxHappy = -sys.maxsize
        peopleList = list(self._people)
        last = peopleList.pop()
        # since table is circular, only need to compute permutations of n-1
        for i in permutations(peopleList):
            j = list(i) + [last]
            k = self.getSumHappiness(j)
            if k > maxHappy:
                maxHappy = k
                maxList = j

        return maxHappy, maxList


def parseInstruct(instructs):
    a = Table()
    for i in instructs:
        personA, _, direction, num, _, _, _, _, _, _, personB = i.split()
        personB = personB.strip('.')
        num = int(num)
        if direction == 'lose':
            num *= -1
        a.addPerson(personA)
        a.addScore(personA, personB, num)
    return a

def addMe(table):
    for i in table._people:
        table.addScore(i, 'me', 0)
        table.addScore('me', i, 0)
    table.addPerson('me')

f = None
with open('advent13data.txt') as d:
    f = d.read().strip().split('\n')

a = parseInstruct(f)
happyA, listA = a.getMaxHappiness()
addMe(a)
happyB, listB = a.getMaxHappiness()

print('optimal happy: {0}\noptimal happy with me: {1}\ndifference: {2}'.format(happyA, happyB, happyB - happyA))
