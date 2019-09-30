import sys

input = sys.stdin.readline


def main():
    text = {
        25: "Christmas",
        24: "Christmas Eve",
        23: "Christmas Eve Eve",
        22: "Christmas Eve Eve Eve",
    }
    print(text[int(input())])


if __name__ == "__main__":
    main()
