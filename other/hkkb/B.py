import sys

input = sys.stdin.readline


def main():
    h, w = map(int, input().split())
    # 右、下のチェック
    cnt = 0
    t = [[s == "#" for s in input().strip()] for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if t[i][j]:
                continue
            if j < (w - 1) and not t[i][j + 1]:
                cnt += 1
            if i < (h - 1) and not t[i + 1][j]:
                cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()
