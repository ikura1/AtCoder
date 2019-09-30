import sys

input = sys.stdin.readline


def main():
    rep = {"1": "9", "9": "1"}
    print("".join([rep.get(c, c) for c in input().strip()]))


if __name__ == "__main__":
    main()
