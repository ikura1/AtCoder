import sys

input = sys.stdin.readline


def main():
    n = list(range(1, int(input()) + 1))
    print(len([i for i in n if i % 2 == 1]) / len(n))


if __name__ == "__main__":
    main()
