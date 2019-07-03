import sys

input = sys.stdin.readline


def main():
    s, t = [int(i) for i in input().split()]
    print(t - s + 1)


if __name__ == "__main__":
    main()
