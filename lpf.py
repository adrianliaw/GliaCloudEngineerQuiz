def lpf(n):
    largest = 2
    while True:
        if largest ** 2 > n:
            if n > 1:
                return n
            return largest
        if n == 1:
            return largest
        if n % largest == 0:
            n /= largest
            continue
        largest += 1


print(lpf(600851475143))
