import sys

input = sys.stdin.readline


def main():
    p, q, r = [int(i) for i in input().split()]
    times = [p, q, r]
    print(sum(times) - max(times))


if __name__ == "__main__":
    main()
