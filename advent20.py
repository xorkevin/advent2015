# import numpy as np
#
#
# def part_one():
#     with open("advent20data.txt") as fin:
#         puzzle_input = int(fin.read().strip())
#     max_number = puzzle_input // 10
#     houses = np.zeros(max_number + 1)
#     for i in range(1, max_number + 1):
#         houses[i:max_number:i] += 10 * i
#     print(np.where(houses >= puzzle_input)[0][0])
#
#
# def part_two():
#     with open("advent20data.txt") as fin:
#         puzzle_input = int(fin.read().strip())
#     max_number = puzzle_input // 10
#     houses = np.zeros(max_number + 1)
#     for i in range(1, max_number + 1):
#         houses[i:i * 50:i] += 10 * i
#     print(np.where(houses >= puzzle_input)[0][0])
#
#
# if __name__ == '__main__':
#     part_one()
#     part_two()

from itertools import count
from math import sqrt


def factors(n):
    results = set()
    for i in range(1, int(sqrt(n)) + 1):
        div, mod = divmod(n, i)
        if mod == 0:
            results.add(i)
            results.add(div)
    return results


def get_n_gifts(number, gifts_per_number=10, limit=None):
    if limit is None:
        n_visits = sum(i for i in factors(number))
    else:
        n_visits = sum(i for i in factors(number) if number <= i * limit)
    return n_visits * gifts_per_number


def get_house_n_gifts(n, gifts_per_number=10, limit=None):
    for i in count(1):
        if get_n_gifts(i, gifts_per_number, limit) >= n:
            return i


def part_one():
    with open("advent20data.txt") as fin:
        puzzle_input = int(fin.read().strip())
    print(get_house_n_gifts(puzzle_input))


def part_two():
    with open("advent20data.txt") as fin:
        puzzle_input = int(fin.read().strip())
    print(get_house_n_gifts(puzzle_input, 11, 50))

if __name__ == "__main__":
    part_one()
    part_two()
