import sys

input = sys.stdin.readline


def main():
    print(sum([s == t for s, t in zip(input(), input())][:-1]))


if __name__ == "__main__":
    main()
