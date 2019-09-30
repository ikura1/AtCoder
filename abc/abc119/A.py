import sys

input = sys.stdin.readline


def main():
    print("Heisei" if int("".join(input().split("/"))) <= 20190430 else "TBD")


if __name__ == "__main__":
    main()
