dict = {}
keys = range(101, 110, 1)

for i in keys:
    dict[i] = 0

sums = [102, 102, 102, 102, 102, 102, 102, 102, 102, 103, 104, 104, 104, 109]

for s in sums:
    dict[s] += 1

print(dict)
