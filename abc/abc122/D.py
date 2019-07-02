import sys


def main():
    input = sys.stdin.readline
    # n = int(input())
    m = 1000000007
    n = 4
    chars = [0, 1, 2, 3]
    dp = [[[[c for c in chars] for b in chars] for a in chars] for i in range(n)]
    print(len(dp))


if __name__ == "__main__":
    main()
