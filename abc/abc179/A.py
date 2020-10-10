import sys

input = sys.stdin.readline


def main():
    s = input().strip()
    print(s + "es" if s[-1] == "s" else s + "s")


if __name__ == "__main__":
    main()
