inp = 'cqjxjnds'


def increment(phrase, n):
    l = list(map(lambda x: (ord(x)-97)%26, list(phrase)))
    b = len(l)

    l[b-1] += n

    carry = 0
    for i in reversed(range(0, b)):
        l[i] += carry
        carry = int(l[i]/26)
        l[i] %= 26
        if carry == 0:
            break
    if carry > 0:
        l.insert(0, carry)

    a = ''
    for i in l:
        a += chr(i + 97)
    return a


def has_triple(phrase):
    l = len(phrase)
    if l < 3:
        return False

    for i in range(2, l):
        if ord(phrase[i]) - ord(phrase[i-1]) == 1 and ord(phrase[i]) - ord(phrase[i-2]) == 2:
            return True

    return False


def has_double(phrase):
    l = len(phrase)
    if l < 4:
        return False

    i = 1
    a = 0
    while i < l:
        if phrase[i] == phrase[i-1]:
            a += 1
            i += 1
        if a > 1:
            return True
        i += 1

    return False


def has_banned(phrase):
    return 'i' in phrase or 'o' in phrase or 'l' in phrase


def find_next_pass(phrase):
    it = 0
    k = phrase
    while not has_triple(k) or not has_double(k) or has_banned(k):
        k = increment(k, 1)
        # print(k)
        if it % 100000 == 0:
            print('iter {0}'.format(it), flush=True)
        it += 1
    return k


# start

password1 = find_next_pass(inp)
password2 = find_next_pass(increment(password1, 1))
print('password 1: {0}\npassword 2: {1}'.format(password1, password2))
