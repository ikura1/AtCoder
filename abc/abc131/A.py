import sys

input = sys.stdin.readline


def main():
    s = input()
    print("Bad" if any([s[i - 1] == s[i] for i in range(1, 4)]) else "Good")


if __name__ == "__main__":
    main()
