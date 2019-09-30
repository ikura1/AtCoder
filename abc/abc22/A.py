import sys

input = sys.stdin.readline


def best(a, b, c):
    return b <= a <= c


def main():
    n, s, t = map(int, input().split())
    w = int(input())
    cnt = int(best(w, s, t))
    for _ in range(n - 1):
        w += int(input())
        if best(w, s, t):
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()
