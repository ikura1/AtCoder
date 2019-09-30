import sys

input = sys.stdin.readline


def main():
    s = input()
    if "a" in s and "b" in s and "c" in s:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
