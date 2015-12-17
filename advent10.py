inp = 3113322113

def lookAndSay(num, k):
    num = str(num)
    if k == 0:
        return num

    newNum = ''

    lastNum = ''
    lastCount = 0
    for i in num:
        if i != lastNum:
            if lastCount > 0:
                newNum += str(lastCount) + lastNum
            lastNum = i
            lastCount = 0
        lastCount += 1
    if lastCount > 0:
        newNum += str(lastCount) + lastNum

    return lookAndSay(newNum, k-1)
    return newNum

a = lookAndSay(inp, 40)
b = lookAndSay(a, 10)

print('length of out 40: {0}\nlength of out 50: {1}'.format(len(a), len(b)))
