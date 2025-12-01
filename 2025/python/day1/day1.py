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
        d = int(datum[1:])
        while d > 0:
            dial -= 1
            d -= 1
            dial %= 100
            if dial == 0:
                pw += 1
    elif datum[0] == 'R':
        d = int(datum[1:])
        while d > 0:
            dial += 1
            dial %= 100
            d -= 1
            if dial == 0:
                pw += 1
    else:
        print("unknown data element")

print(f"password: {pw}")
