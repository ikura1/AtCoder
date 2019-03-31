import sys

input = sys.stdin.readline


def main():
    a = int(input())
    b, c = [int(i) for i in input().split()]
    s = input().strip()
    print("{} {}".format(a + b + c, s))


if __name__ == "__main__":
    main()
