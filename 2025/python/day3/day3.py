import sys

filename = sys.argv[1]

with open(filename, "r") as f:
    data = f.read().strip().split("\n")

joltages = []
for datum in data:
    low_max_idx = 0
    high_max_idx = len(datum)-1

    low_idx = low_max_idx+1
    while low_idx < high_max_idx:
        if datum[low_idx] > datum[low_max_idx]:
            low_max_idx = low_idx

        low_idx += 1

    high_idx = high_max_idx-1
    while high_idx > low_max_idx:
        if datum[high_idx] > datum[high_max_idx]:
            high_max_idx = high_idx

        high_idx -= 1

    joltages.append(int(str(datum[low_max_idx])+str(datum[high_max_idx])))


print(f"Output Joltage: {sum(joltages)}")
