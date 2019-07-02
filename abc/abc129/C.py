import sys
from itertools import accumulate

input = sys.stdin.readline


def main():
    n, m = [int(i) for i in input().split()]
    a_list = [int(input()) for _ in range(m)]
    if any([a + 1 == a_list[i + 1] for i, a in enumerate(a_list[:-1])]):
        print(0)
        return
    takahashi = 0
    kakuritu = []
    for a in a_list:
        (n, a - 1)
        n = a + 1
    print(1)
    # print(hoge / 1000000007)


if __name__ == "__main__":
    main()
