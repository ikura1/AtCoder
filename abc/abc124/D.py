import sys

input = sys.stdin.readline


def mizikashi():
    n, k = map(int, input().split())
    s, = input()

    # 連続の配列
    t = 1
    g = []
    for i in range(1, n):
        if s[i] == s[i - 1]:
            t += 1
        else:
            g.append(t)
            t = 1
    g.append(t)

    # 1から2, 2から3に値を足していく？？
    # 累積和？
    for i in range(1, len(g)):
        g[i] += g[i - 1]
    # 始点と終点を追加
    g = [0] + g + [g[-1]]
    a = 0
    # なんかやっているが疲れてて読めない
    for i in range(s[0] == "1", len(g), 2):
        a = max(a, g[i] - g[max(0, i - 2 * k - 1)])
    print(a)


def main():
    n, k = [int(i) for i in input().split()]
    s = input()
    # 連続の見つけ方
    # 既存の1の連続数
    # 既存の0の連続数
    #
    # Kの指示数と0の数


if __name__ == "__main__":
    main()
