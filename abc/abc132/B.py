import sys

input = sys.stdin.readline


def main():
    n = int(input())
    count = 0
    p_list = [int(i) for i in input().split()]
    for i in range(1, n - 1):
        hoge = p_list[i - 1 : i + 2]
        if min(hoge) == p_list[i]:
            continue
        if len(set(hoge)) == 3 and max(hoge) == p_list[i]:
            continue
        count += 1
    print(count)


if __name__ == "__main__":
    main()
