from itertools import permutations, combinations

numbers = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,25,50,75,100] # All the numbers in the Countdown rules
ds = set()
ls = set()
i = 0

# n = list(combinations(numbers, 6))
# n.sort()
n = sorted(combinations(numbers, 6))
for item in n:
    ds.add(item)

for eq in ds:
    for var in permutations(eq):
        if var not in ls:
            ls.add(var)
        i += 1

print(f'Without dupes: {len(ls)}')
print(f'        Total: {i}')