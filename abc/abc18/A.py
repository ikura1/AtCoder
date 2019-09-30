import sys

input = sys.stdin.readline


def main():
    a, b, c = [int(input()) for _ in range(3)]
    for i in [a, b, c]:
        print(3 - sorted([a, b, c]).index(i))


if __name__ == "__main__":
    main()
