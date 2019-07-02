import sys


def main():
    input = sys.stdin.readline
    ryori_list = [int(input()) for _ in range(5)]
    loss_list = [10 - (r % 10) for r in ryori_list if r % 10] or [0]
    print(sum(ryori_list) + sum(loss_list) - max(loss_list))


if __name__ == "__main__":
    main()
