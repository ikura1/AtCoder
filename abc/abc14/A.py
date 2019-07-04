import sys

input = sys.stdin.readline


def main():
    i = int(input())
    j = int(input())
    print(0 if i % j == 0 else j - i % j)


if __name__ == "__main__":
    main()
