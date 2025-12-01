import sys
if len(sys.argv) < 2:
    print("requires an input file")
    exit(1)

filename = sys.argv[1]

data = []
with open(filename, "r") as f:
    data = f.read().strip().split("\n")

pw = 0
dial = 50
for datum in data:
    if datum[0] == 'L':
        dial -= int(datum[1:])
        dial %= 100
    elif datum[0] == 'R':
        dial += int(datum[1:])
        dial %= 100
    else:
        print("unknown data element")

    if dial == 0:
        pw += 1


print(f"password: {pw}")
