import sys

input = sys.stdin.readline


def main():
    # 無指向グラフの存在確認
    # 単純かつ連結
    # 頂点は1...N
    # グラフの辺数はM
    # 最短距離が2であるような頂点対(i, j)がK個存在
    N, K = [int(i) for i in input().split()]
    # 全探索の方法もすぐ出てこない…


if __name__ == "__main__":
    main()
