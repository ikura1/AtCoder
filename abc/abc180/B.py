import sys
import math

input = sys.stdin.readline


def main():
    n = int(input())
    x_list = list(map(int, input().split()))
    x_abs = [abs(x) for x in x_list]

    u = math.sqrt(sum([x ** 2 for x in x_abs]))
    print(sum(x_abs))
    print(u)
    print(max(x_abs))


if __name__ == "__main__":
    main()
