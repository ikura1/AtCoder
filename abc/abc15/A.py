import sys

input = sys.stdin.readline


def main():
    i = input()
    j = input()
    print(max([i, j], key=len))


if __name__ == "__main__":
    main()
