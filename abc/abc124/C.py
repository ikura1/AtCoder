import sys

input = sys.stdin.readline


def main():
    s = input().strip()
    length = len(s)
    o = "10" * (length // 2 + (length % 2))
    o_len = len([i for i, j in zip(s, o) if i == j])
    z_len = len([i for i, j in zip(s, o[::-1]) if i == j])
    print(length - max([z_len, o_len]))


if __name__ == "__main__":
    main()
