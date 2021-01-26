def bp(x1, x2):
    if x1 > 0 and x2 > 0:
        return 0
    else:
        return x1 + x2


def mb(x):
    b = ''
    while x > 0:
        b = str(x % 2) + b
        x = x // 2
    if b == '':
        return 0
    else:
        return int(b)


i = 0
while i < 2 ** 4:
    x1 = mb(i) // 1000
    x2 = (mb(i) % 1000) // 100
    x3 = (mb(i) % 100) // 10
    x4 = mb(i) % 10
    f = bp(x1 * x2, x4)
    print(x1, x2, x3, x4, f, sep=' ')
    i += 1