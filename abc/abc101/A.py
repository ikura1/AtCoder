import sys

input = sys.stdin.readline


def main():
    print(sum([1 if c == "+" else -1 for c in input().strip()]))


if __name__ == "__main__":
    main()
