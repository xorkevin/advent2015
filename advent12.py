import json


def tree_search(tree, check_red = False):
    if type(tree) == int:
        return tree
    elif type(tree) == list:
        return sum(map(lambda x: tree_search(x, check_red), tree))
    elif type(tree) == dict:
        if check_red and 'red' in tree.values():
            return 0
        return tree_search(list(tree.values()), check_red)
    return 0


f = None
with open('advent12data.txt') as d:
    f = json.loads(d.read().strip())

print('sum of numbers: {0}\nsum of numbers without red: {1}'.format(tree_search(f), tree_search(f, True)))
