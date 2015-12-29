# google ortools required
# def day15(names, caps, durs, flavs, texts, cals, calorie_total=None):
#     solver = pywrapcp.Solver('AOC Day 15')
#
#     ingredients = []
#     for name in names:
#         ingredient = solver.IntVar(range(0, 100), name)
#         solver.Add(ingredient >= 0)
#         ingredients.append(ingredient)
#
#     solver.Add(solver.Sum(ingredients) == 100)
#     cap_sum = solver.Sum(
#         caps[i] * ingredients[i] for i in xrange(0, len(ingredients)))
#     dur_sum = solver.Sum(
#         durs[i] * ingredients[i] for i in xrange(0, len(ingredients)))
#     flav_sum = solver.Sum(
#         flavs[i] * ingredients[i] for i in xrange(0, len(ingredients)))
#     text_sum = solver.Sum(
#         texts[i] * ingredients[i] for i in xrange(0, len(ingredients)))
#     solver.Add(cap_sum >= 0)
#     solver.Add(dur_sum >= 0)
#     solver.Add(flav_sum >= 0)
#     solver.Add(text_sum >= 0)
#
#     if calorie_total is not None:
#         cal_sum = solver.Sum(
#             cals[i] * ingredients[i] for i in xrange(0, len(ingredients)))
#         solver.Add(cal_sum == calorie_total)
#
#     total = solver.IntVar(0, sys.maxint, "Total")
#     solver.Add(total == cap_sum * dur_sum * flav_sum * text_sum)
#     objective = solver.Maximize(total, 1)
#
#     db = solver.Phase(ingredients + [total],
#                       solver.INT_VAR_DEFAULT,
#                       solver.INT_VALUE_DEFAULT)
#
#     solver.NewSearch(db, [objective])
#
#     best = None
#     best_ingredients = None
#     while solver.NextSolution():
#         best = total.Value()
#         best_ingredients = [(i.Name(), i.Value()) for i in ingredients]
#
#     print("Best total: {}, with: {}".format(best, best_ingredients))
#
#     solver.EndSearch()

def process_line(l):
    x = l.replace(',', '').split()
    return (int(x[2]), int(x[4]), int(x[6]), int(x[8]), int(x[10]), x[0])

def calculate_vector(data, x1, x2, x3, x4):
    r1 = data[0][0] * x1 + data[1][0] * x2 + data[2][0] * x3 + data[3][0] * x4
    r2 = data[0][1] * x1 + data[1][1] * x2 + data[2][1] * x3 + data[3][1] * x4
    r3 = data[0][2] * x1 + data[1][2] * x2 + data[2][2] * x3 + data[3][2] * x4
    r4 = data[0][3] * x1 + data[1][3] * x2 + data[2][3] * x3 + data[3][3] * x4
    if r1 <= 0 or r2 <= 0 or r3 <= 0 or r4 <= 0:
        return 0
    return r1 * r2 * r3 * r4

def calculate_vector_2(data, x1, x2, x3, x4):
    r1 = data[0][0] * x1 + data[1][0] * x2 + data[2][0] * x3 + data[3][0] * x4
    r2 = data[0][1] * x1 + data[1][1] * x2 + data[2][1] * x3 + data[3][1] * x4
    r3 = data[0][2] * x1 + data[1][2] * x2 + data[2][2] * x3 + data[3][2] * x4
    r4 = data[0][3] * x1 + data[1][3] * x2 + data[2][3] * x3 + data[3][3] * x4
    r5 = data[0][4] * x1 + data[1][4] * x2 + data[2][4] * x3 + data[3][4] * x4
    if r5 != 500:
        return -1
    if r1 <= 0 or r2 <= 0 or r3 <= 0 or r4 <= 0:
        return 0
    return r1 * r2 * r3 * r4

data = []
for l in open('advent15data.txt').readlines():
    data.append(process_line(l))

# Part 1
t = -1
for x1 in range(0, 101):
    for x2 in range(0, 101 - x1):
        for x3 in range(0, 101 - x1 - x2):
            x4 = 100 - x1 - x2 - x3
            x = calculate_vector(data, x1, x2, x3, x4)
            if x > t:
                t = x
print(t)

# Part 2
t = -1
for x1 in range(0, 101):
    for x2 in range(0, 101 - x1):
        for x3 in range(0, 101 - x1 - x2):
            x4 = 100 - x1 - x2 - x3
            x = calculate_vector_2(data, x1, x2, x3, x4)
            if x > t:
                t = x
print(t)
