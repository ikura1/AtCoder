import sys
import math

input = sys.stdin.readline


def eratosthenes(limit):
    A = [i for i in range(2, limit + 1)]
    P = []

    while True:
        prime = min(A)

        if prime > math.sqrt(limit):
            break
        P.append(prime)
        i = 0
        while i < len(A):
            if A[i] % prime == 0:
                A.pop(i)
                continue
            i += 1
    for a in A:
        P.append(a)
    return P


def divisor(n):
    i = 1
    table = []
    while i * i <= n:
        if n % i == 0:
            table.append(i)
            table.append(n // i)
        i += 1
    table = list(set(table))
    return table


def main():
    # 素数
    n = int(input())
    # for i in range(1, n // 2 + 1):
    #     if n % i == 0:
    #         print(i)
    for i in sorted(divisor(n)):
        print(i)


if __name__ == "__main__":
    main()
