from itertools import groupby, count
data = input()

print(*[(len(list(g)), int(k)) for k, g in groupby(data)])
