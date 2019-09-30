import sys

input = sys.stdin.readline


def main():
    tenki = {"Sunny": "Cloudy", "Cloudy": "Rainy", "Rainy": "Sunny"}
    print(tenki[input().strip()])


if __name__ == "__main__":
    main()
