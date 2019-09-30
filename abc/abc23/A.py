import sys

input = sys.stdin.readline


def main():
    print(sum([int(i) for i in input().strip()]))


if __name__ == "__main__":
    main()
