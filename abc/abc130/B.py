import sys

input = sys.stdin.readline


def main():
    n, x = [int(i) for i in input().split()]
    l_list = [int(i) for i in input().split()]
    n += 1
    d = 0
    num = 1
    for i in range(1, n):
        d = d + l_list[i - 1] * (i <= n + 1)
        if d > x:
            break
        num += 1
    print(num)


if __name__ == "__main__":
    main()
