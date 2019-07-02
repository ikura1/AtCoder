import sys
import re

input = sys.stdin.readline


def main():
    n = int(input())
    s = input()

    # 白の数
    w = s.count(".")
    # ほげの数
    m = w
    for c in s:
        if c == ".":
            # a
            w -= 1
            if w < m:
                # mの方が大きいと、wに入れる
                m = w
        elif c == "#":
            # 黒の場合、wに加える……？
            w += 1
    print(m)


if __name__ == "__main__":
    main()
