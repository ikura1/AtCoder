import sys

input = sys.stdin.readline


def main():
    n = int(input())
    a = [int(i) for i in input().split() if i != "0"]
    print(sum(a) // len(a) + (sum(a) % len(a) != 0))


if __name__ == "__main__":
    main()
