import sys

input = sys.stdin.readline


def main():
    # 平面上にN個の点がある
    # i番目の座業は(Xi, Yi)
    # (a, b), (a, d), (c, b), (c, d)に3点存在する場合、一箇所に点を追加する
    # この動作が何回行えるか
    N = int(input())
    points = [[int(i) for i in input().split()] for _ in range(N)]
    # 全探索は書ける気はするが、10**5か…
    # 問題的に組合せかな
    # あと組み合わせ後にさらに組合せなやつだな


if __name__ == "__main__":
    main()
