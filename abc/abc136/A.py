import sys

input = sys.stdin.readline


def main():
    a, b, c = [int(i) for i in input().split()]
    d = c - (a - b)
    print(d if d > 0 else 0)


if __name__ == "__main__":
    main()
