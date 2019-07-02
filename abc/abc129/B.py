import sys
from itertools import accumulate

input = sys.stdin.readline


def main():
    n = int(input())
    w_list = [int(i) for i in input().split()]
    sum_ = sum(w_list)
    min_ = None
    for s1 in accumulate(w_list):
        s2 = sum_ - s1
        s12 = abs(s1 - s2)
        if min_ is None:
            min_ = s12
        if s12 <= min_:
            min_ = s12
        else:
            break
    print(min_)


if __name__ == "__main__":
    main()
