import sys

input = sys.stdin.readline


def main():
    n = int(input())
    cnt = 0
    for a in range(1, n):
        print(n - 1, a, (n - 1) // a)
        cnt += (n - 1) // a
    print(cnt)


if __name__ == "__main__":
    main()
