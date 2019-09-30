import sys

input = sys.stdin.readline


def main():
    print(sorted([int(i) for i in input().split()])[1])


if __name__ == "__main__":
    main()
