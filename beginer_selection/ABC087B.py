import sys
from itertools import product

input = sys.stdin.readline


def main():
    a = [i * 500 for i in range(int(input()) + 1)] or [0]
    b = [i * 100 for i in range(int(input()) + 1)] or [0]
    c = [i * 50 for i in range(int(input()) + 1)] or [0]
    x = int(input())
    all_ = [[i, j, k] for i, j, k in product(a, b, c)]
    print(len([i for i in all_ if sum(i) == x]))


if __name__ == "__main__":
    main()
