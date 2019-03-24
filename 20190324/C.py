# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import sys
from itertools import accumulate


def main():
    input = sys.stdin.readline
    n, q = [int(i) for i in input().split()]
    s = input().strip()
    qs = [[int(i) for i in input().split()] for _ in range(q)]
    hoges = [0] + [1 if s[i : i + 2] == "AC" else 0 for i in range(n - 1)]
    hoges = list(accumulate(hoges))
    for (l, r) in qs:
        print(hoges[r - 1] - hoges[l - 1])


if __name__ == "__main__":
    main()
