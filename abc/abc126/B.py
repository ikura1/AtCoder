import sys

input = sys.stdin.readline


def check_format(num):
    if not num:
        return 0
    if num <= 12:
        return 1
    return 2


def main():
    s = input()
    f = int(s[:2])
    b = int(s[2:])
    f_format = check_format(f)
    b_format = check_format(b)
    format_ = "AMBIGUOUS"
    if set([f_format, b_format]) == {2}:
        format_ = "NA"
    if set([f_format, b_format]) == {0}:
        format_ = "NA"
    if [f_format, b_format] == [0, 2] or [f_format, b_format] == [2, 0]:
        format_ = "NA"
    if f_format == 1 and b_format in (0, 2):
        format_ = "MMYY"
    if f_format in (0, 2) and b_format == 1:
        format_ = "YYMM"
    print(format_)


if __name__ == "__main__":
    main()
