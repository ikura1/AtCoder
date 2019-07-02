import sys

input = sys.stdin.readline


def main():
    W, H, x, y = [int(i) for i in input().split()]
    min_x = 0
    min_y = 0
    areas = []
    if 0 < x < W:
        area_a = x * H
        area_b = (W - x) * H
        areas.append(min([area_a, area_b]))

    if 0 < y < H:
        area_a = W * y
        area_b = W * (H - y)
        areas.append(min([area_a, area_b]))

    multi_flag = 0
    if len(areas) > 1 and len(set(areas)) == 1:
        multi_flag = 1
    min_area = 0
    if areas:
        min_area = max(areas)
        print(min_area, multi_flag)
        return
    


if __name__ == "__main__":
    main()
