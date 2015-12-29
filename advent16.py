# import re
#
# ref = { "children": lambda x: x == 3,
#         "cats": lambda x: x > 7,
#         "trees": lambda x: x > 3,
#         "samoyeds": lambda x: x == 2,
#         "akitas": lambda x: x == 0,
#         "vizslas": lambda x: x == 0,
#         "pomeranians": lambda x: x < 3,
#         "goldfish": lambda x: x < 5,
#         "cars": lambda x: x == 2,
#         "perfumes": lambda x: x == 1 }
#
# with open('advent16data.txt') as fh:
#     p = re.compile(r'^Sue ([0-9]+): ([A-Za-z]+): ([0-9]+), ([A-Za-z]+): ([0-9]+), ([A-Za-z]+): ([0-9]+)$')
#     for l in fh:
#         match = p.findall(l.strip())[0]
#         nr = match[0]
#         things = dict(zip([name for i, name in enumerate(match[1:]) if i % 2 == 0],
#                           [int(count) for i, count in enumerate(match[1:]) if i % 2 == 1]))
#
#         if sum([ref[k](v) and 1 or 0 for k,v in things.items()]) == 3:
#             print(nr, things)


def DaySixteen1():

    file = 'advent16data.txt'
    with open(file, 'r') as f:
        lines = f.readlines()

    # for each line, split it and add entry to dictionary with the sue's number as key, and a dict of what we know about them as the value
    sues = {}
    for line in lines:
        l = line.split()
        sues[int(l[1][:-1])] = {
            l[2][:-1]:int(l[3][:-1]),
            l[4][:-1]:int(l[5][:-1]),
            l[6][:-1]:int(l[7])
            }

    # dict comprehension with tuples as 'name':number

    auntSue = {x.split()[0][:-1]:int(x.split()[1]) for x in '''children: 3
    cats: 7
    samoyeds: 2
    pomeranians: 3
    akitas: 0
    vizslas: 0
    goldfish: 5
    trees: 3
    cars: 2
    perfumes: 1'''.split('\n')}

    # check each sue (n) and check for each thing that auntSue has (i) if they also have that number
    for n in range(1, 501):
        count = 0
        for i in auntSue.keys():
            try:
                if sues[n][i] == auntSue[i]:
                    count += 1
            except KeyError:
                continue
        if count == 3:
            print(n)

def DaySixteen2():

    # same as above up to the end of the auntSue assignment
    file = 'advent16data.txt'
    with open(file, 'r') as f:
        lines = f.readlines()

    # for each line, split it and add entry to dictionary with the sue's number as key, and a dict of what we know about them as the value
    sues = {}
    for line in lines:
        l = line.split()
        sues[int(l[1][:-1])] = {
            l[2][:-1]:int(l[3][:-1]),
            l[4][:-1]:int(l[5][:-1]),
            l[6][:-1]:int(l[7])
            }

    # dict comprehension with tuples as 'name':number

    auntSue = {x.split()[0][:-1]:int(x.split()[1]) for x in '''children: 3
    cats: 7
    samoyeds: 2
    pomeranians: 3
    akitas: 0
    vizslas: 0
    goldfish: 5
    trees: 3
    cars: 2
    perfumes: 1'''.split('\n')}

    # same as above but with an expanded if statement to catch the changes
    for n in range(1, 501):
        count = 0
        for i in auntSue.keys():
            try:
                if i == 'cats' or i == 'trees':
                    if sues[n][i] > auntSue[i]:
                        count += 1
                elif i == 'goldfish' or i == 'pomeranians':
                    if sues[n][i] < auntSue[i]:
                        count += 1
                else:
                    if sues[n][i] == auntSue[i]:
                        count += 1
            except KeyError:
                continue
        if count == 3:
            print(n)

DaySixteen1()
DaySixteen2()
