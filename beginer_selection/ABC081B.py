import sys

input = sys.stdin.readline


def waru(a_list, n=0):
    hoge = []
    for a in a_list:
        q, mod = divmod(a, 2)
        if mod == 1:
            return n
        hoge.append(q)
    return waru(hoge, n + 1)


def main():
    n = int(input())
    a_list = [int(i) for i in input().split()]
    # 全探索するなら

    print(waru(a_list))


if __name__ == "__main__":
    main()
