import re
row = 'ATCODER'
lenght = len(row)
max_moji = 0
for i in range(lenght):
    if row[i] in 'ACGT':
        print(row[i])
        moji = 1
        for j in range(i + 1, lenght):
            print(row[j])
            if row[j] in 'ACGT':
                moji += 1
            else:
                break
        max_moji = moji if moji > max_moji else max_moji
    if max_moji == lenght - i:
        break
print(max_moji)
