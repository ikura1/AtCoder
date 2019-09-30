import sys

input = sys.stdin.readline


def main():
    a, b = [int(i) for i in input().split()]
    k = (a + b) // 2
    if abs(a - k) == abs(b - k):
        print(k)
    else:
        print("IMPOSSIBLE")


if __name__ == "__main__":
    main()
