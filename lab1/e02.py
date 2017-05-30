def primary(n):
    def rec(res, ls):
        if len(ls) == 0:
            return res
        elif all(ls[0] % x != 0 for x in res):
            return rec(res + ls[:1], [y for y in ls[1:] if y % ls[0] != 0])
        else:
            return rec(res, ls[1:])

    r = [i for i in range(1, n+1) if n % i == 0]
    return rec([], range(2, n)), r


print primary(1000)
