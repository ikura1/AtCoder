import sys
from itertools import accumulate

input = sys.stdin.readline


def main():
    n = int(input())
    d_list = sorted([int(i) for i in input().split()])
    print(d_list[n // 2] - d_list[n // 2 - 1])
    # print(list(accumulate(d_list, max)))
    # K 選び方でARC と ABCが同じ数になる選び当た


if __name__ == "__main__":
    main()
