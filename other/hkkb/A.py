import sys

input = sys.stdin.readline


def main():
    s = input().strip()
    t = input().strip()
    print(t.upper() if s == "Y" else t)


if __name__ == "__main__":
    main()
