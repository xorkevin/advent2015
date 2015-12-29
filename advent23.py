# with open('advent23data.txt') as d:
#     program = d.read().strip().split('\n')
#
# regs = {'a': 0, 'b': 0}
# i = 0
# while True:
#     if i not in range(len(program)):
#         break
#     line = program[i]
#     inst, r = line.split(' ', 1)
#     di = 1
#     if inst == 'hlf':
#         regs[r] //= 2
#     elif inst == 'tpl':
#         regs[r] *= 3
#     elif inst == 'inc':
#         regs[r] += 1
#     elif inst == 'jmp':
#         di = int(r)
#     elif inst == 'jie':
#         r, offset = r.split(',')
#         if regs[r] % 2 == 0:
#             di = int(offset)
#     elif inst == 'jio':
#         r, offset = r.split(',')
#         if regs[r] == 1:
#             di = int(offset)
#     else:
#         raise ValueError(line)
#     i += di
# print(regs['b'])

program = [i.strip().split(' ', 1) for i in open('advent23data.txt').readlines()]

registers = {'a': 0, 'b': 0, 'pc': 0}

def hlf(args):
    registers[args] >>= 1
    registers['pc'] += 1

def tpl(args):
    registers[args] *= 3
    registers['pc'] += 1

def inc(args):
    registers[args] += 1
    registers['pc'] += 1

def jmp(args):
    registers['pc'] += int(args)

def jie(args):
    r, o = args.split(', ')
    if registers[r] % 2 == 0:
        registers['pc'] += int(o)
    else:
        registers['pc'] += 1

def jio(args):
    r, o = args.split(', ')
    if registers[r] == 1:
        registers['pc'] += int(o)
    else:
        registers['pc'] += 1

instructions = {'hlf': hlf, 'tpl': tpl, 'inc': inc, 'jmp': jmp, 'jie': jie, 'jio': jio}

# Part 1
registers = {'a': 0, 'b': 0, 'pc': 0}

while registers['pc'] < len(program):
    instructions[program[registers['pc']][0]](program[registers['pc']][1])
print(registers)

# Part 2
registers = {'a': 1, 'b': 0, 'pc': 0}

while registers['pc'] < len(program):
    instructions[program[registers['pc']][0]](program[registers['pc']][1])
print(registers)
