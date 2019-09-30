import sys

input = sys.stdin.readline


def main():
    a, b, c, d = map(int, input().split())
    T = b / a
    A = d / c
    if T == A:
        print("DRAW")
    elif T > A:
        print("TAKAHASHI")
    else:
        print("AOKI")


if __name__ == "__main__":
    main()
