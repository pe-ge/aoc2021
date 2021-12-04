depths = list(map(int, open("input.txt").read().split()))

prev_val = depths[0]
count = 0
for d in depths[1:]:
    if d > prev_val:
        count += 1
    prev_val = d
print(count)

prev_val = sum(depths[0:3])
count = 0
for idx in range(1, len(depths)):
    val = sum(depths[idx:idx+3])
    if val > prev_val:
        count += 1
    prev_val = val

print(count)
