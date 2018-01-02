# Uses python3
def calc_fib(n):
    return calc_fib_acc(n, 0, 1)

def calc_fib_acc(n, a, b):
    if (n <= 0):
        return a
    return calc_fib_acc(n-1, b, a+b)

def fib_m(n, m):
    if n <= 1:
        return n
    pl = [0,1]
    for i in range(n - 1):
        current = (pl[-2]+pl[-1])%m
        previous = pl[-1]
        if (previous, current) == (0,1):
            num = i+1
            return pl[n%num]
        pl.append(current)
    return pl[-1]

def get_fibonacci_last_digit(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10
    return current

def get_sum_fib(n):
    return (fib_m(n+2, 10) - 1) %10

if __name__ == "__main__":
    n = int(input())
    print(calc_fib(n))
