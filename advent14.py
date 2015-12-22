class Deer:
    def __init__(self, name, speed, time, rest):
        """
        :param name:
        :type name: str
        :param speed:
        :type speed: int
        :param time:
        :type time: int
        :param rest:
        :type rest: int
        :return:
        :rtype: Deer
        """
        self.name = name
        self.speed = speed
        self.time = time
        self.rest = rest
        self.period = self.time + self.rest
        self.position = 0
        self.clock = 0
        self.points = 0

    def tick(self, unit=1):
        """
        :param unit:
        :type unit: int
        :return:
        :rtype:
        """
        u = unit - self.period + self.clock
        self.position += (int(u/self.period) * self.time + min(u%self.period, self.time) + max(self.time - self.clock, 0)) * self.speed
        self.clock = (self.clock+unit)%self.period

    def awardPoint(self, quantity = 1):
        self.points += quantity

    def __lt__(self, other):
        """
        :param other:
        :type other: Deer
        :return:
        :rtype: bool
        """
        return self.position < other.position

    def __gt__(self, other):
        """
        :param other:
        :type other: Deer
        :return:
        :rtype: bool
        """
        return self.position > other.position

    def __repr__(self):
        return '{0} position: {1} points {2}'.format(self.name, self.position, self.points)


def parseInstructs(instructs):
    """
    :param instructs:
    :type instructs: list(str)
    :return:
    :rtype: list(Deer)
    """
    reindeer = []
    for i in instructs:
        j = i.split()
        name, speed, time, rest = j[0], int(j[3]), int(j[6]), int(j[13])
        reindeer.append(Deer(name, speed, time, rest))
    return reindeer

with open('advent14data.txt') as d:
    f = d.read().strip().split('\n')

a = parseInstructs(f)
for i in a:
    i.tick(2503)
b = max(a)
print(a)
a = parseInstructs(f)
for i in range(2503):
    for j in a:
        j.tick()
    k = max(a).position
    for j in a:
        if j.position == k:
            j.points += 1
print(a)
c = 0
d = None
for i in a:
    if i.points > c:
        d = i
        c = i.points

print('distance: {0}\npoints: {1}'.format(b.position, d.points))
