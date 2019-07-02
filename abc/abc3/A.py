import sys

input = sys.stdin.readline


def main():
    N = int(input())
    print(sum(range(1, N + 1)) * 10000 / N)


if __name__ == "__main__":
    main()
