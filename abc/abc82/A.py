import sys
import math

input = sys.stdin.readline


def main():
    a, b = map(int, input().split())
    print(math.ceil(sum([a, b]) / 2))


if __name__ == "__main__":
    main()
