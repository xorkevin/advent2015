from hashlib import md5

secretKey = 'iwrupvqb'


def mine(key, numzeroes):
    zeroes = ''
    for i in range(0, numzeroes):
        zeroes += '0'
    count = 0
    while True:
        if md5((key + str(count)).encode('utf-8')).hexdigest()[:numzeroes] == zeroes:
            break
        else:
            count += 1

        if count%100000 == 0:
            print('iter: {0}'.format(count), flush=True)

    return count

# should print '00000'
# print(md5(('abcdef' + str(609043)).encode('utf-8')).hexdigest()[:5])

print('hashnum5: {0}\nhashnum6: {1}'.format(mine(secretKey, 5), mine(secretKey, 6)))
