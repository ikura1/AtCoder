import sys

input = sys.stdin.readline


def main():
    x, y, a, b = map(int, input().split())
    # 強さはY未満
    # xpは最大値
    # 現状の強さ: X
    xp = 0

    # b優先限界
    # a優先限界
    # 流れ a -> b
    while x * a < y and (x * a) <= (x + b):
        x *= a
        xp += 1

    xp += (y - 1 - x) // b
    print(xp)


if __name__ == "__main__":
    main()
