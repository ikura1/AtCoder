import sys

input = sys.stdin.readline


def main():
    print(max([int(i) for i in input().split()]))


if __name__ == "__main__":
    main()
