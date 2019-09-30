import sys

input = sys.stdin.readline


def main():
    # 数式出てこなかった
    n = int(input())
    print(sum(range(1, n + 1)))


if __name__ == "__main__":
    main()
