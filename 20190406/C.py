import sys


def main():
    input = sys.stdin.readline
    n = int(input())
    nin_list = [int(input()) for _ in range(5)]
    area_list = [n, 0, 0, 0, 0, 0]
    time = 0
    while area_list[5] != n:
        for i in range(4, -1, -1):
            if area_list[i] == 0:
                continue
            move_nin = nin_list[i] if area_list[i] > nin_list[i] else area_list[i]
            area_list[i] -= move_nin
            area_list[i + 1] += move_nin
        time += 1
    print(time)


if __name__ == "__main__":
    main()
