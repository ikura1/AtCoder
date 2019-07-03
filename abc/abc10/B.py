import sys

input = sys.stdin.readline


def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    a = [i - 1 for i in a if i in [2, 4, 5, 6, 8]]
    res = len(a)
    a = [i - 1 for i in a if i in [2, 4, 5, 6, 8]]
    res += len(a)
    a = [i - 1 for i in a if i in [2, 4, 5, 6, 8]]
    res += len(a)
    print(res)


if __name__ == "__main__":
    main()
