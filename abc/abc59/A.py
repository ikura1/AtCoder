import sys

input = sys.stdin.readline


def main():
    print("".join([s[0].upper() for s in input().split()]))


if __name__ == "__main__":
    main()
