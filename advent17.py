# import numpy as np
#
# x = np.vectorize(int)(list(open('advent17data.txt')))
# c = 0
# for i in range(1 << len(x)):
#     t = i
#     s = 0
#     for j in x:
#         if t % 2 == 1:
#             s += j
#         t //= 2
#     if s == 150:
#         c += 1
# print(c)
#

# another solution
# class Memoize(object):
#     def __init__(self, func):
#         self.func = func
#         self.memodict = {}
#     def __call__(self, *args):
#         if not self.memodict.has_key(args):
#             self.memodict[args] = self.func(*args)
#         return self.memodict[args]
#
#  @Memoize
#  def counts1(cap, bottles):
#      if cap == 0:
#          return 1
#          # this combination contains all the water
#      if cap < 0 or len(bottles) == 0:
#          return 0
#          # if negative or out of bottles it doesn't work
#      first = bottles[0]
#      rest = bottles[1:]
#      return counts(cap-first,rest) + counts(cap, rest)
# # counts(cap-first,rest) is how all combinations using first
# # counts(cap, rest) is how many combinations not using first
#
#  @Memoize
#  def counts2(cap, bottles, count=4):
#      if cap == 0 and count==0:
#          return 1
#      # only count possibilities that use exactly count bottles
#      if cap < 0 or len(bottles) == 0:
#          return 0
#      first = bottles[0]
#      rest = bottles[1:]
#      return counts(cap-first,rest, count-1) + counts(cap, rest, count)
#

from itertools import combinations

with open('advent17data.txt') as d:
    inp = d.read().strip()

m = [int(line) for line in inp.split('\n')]

# Part 1 - Sum the number of all combinations that hold 150 L.
total = 0
for i in range(1, len(m)+1):
    total += len([x for x in combinations(m, i) if sum(x) == 150])
print(total)

# Part 2 - Break at the first combination that holds 150 L,
#    that's the smallest. Then just print the total as that's
#    the number of ways you can store 150 L in those containers.
total = 0
for i in range(1, len(m)+1):
    total += len([x for x in combinations(m, i) if sum(x) == 150])
    if total:
        break
print(total)
