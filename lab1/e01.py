def f1(l):
    # przyjmuje l zwraca suma elementow w liscie
    x = 0
    for i in l:
        x += i
    return x

print f1([23, 43, 12])


def f2(l, g):
    # 2 listy l i g, zraca z elementami wspolnymi bez, petla for
    res = []
    for x in l:
        if x in g and x not in res:
            res.append(x)
    return res
    # return list(set(l).intersection(set(g)))
print f2([1, 2, 2, 3, 4], [2, 4, 4, 4, 1, 1])


def f3(l, g, c):
    # 3 arg, 2 listy + - * / .

    def solve(x):
        a, b = x
        if c == '*':
            return a * b
        elif c == '/':
            return a / b
        elif c == '+':
            return a + b
        elif c == '-':
            return a - b
        elif c == '**':
            return a ** b
    return map(solve, zip(l, g))


for o in ['*', '/', '+', '-', '**']:
    print f3([1, 2, 3], [2, 3, 4], o)

