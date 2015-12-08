cache = {}

def combination(n, r):
    if r == 1:
        return n
    if n == r:
        return 1
    if (n, r) in cache:
        return cache[(n, r)]
    result = combination(n - 1, r) + combination(n - 1, r - 1)
    cache[(n, r)] = result
    return result


if __name__ == "__main__":
    print("C(40, 10) =", combination(40, 10))
    print("C(990, 33) =", combination(990, 33))
