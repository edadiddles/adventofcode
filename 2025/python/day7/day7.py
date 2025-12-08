import sys


filename = sys.argv[1]


def run(filename):
    with open(filename, "r") as f:
        data = f.read().split("\n")

    beams = [0] * len(data[0])
    for idx, val in enumerate(data[0]):
        if val == "S":
            beams[idx] = 1

    num_splits = 0
    for row in data[1:]:
        for idx, val in enumerate(row):
            if beams[idx] == 1 and val == "^":
                num_splits += 1
                beams[idx] = 0
                beams[idx-1] = 1
                beams[idx+1] = 1

    print(f"Num Beam Splits: {num_splits}")


run(filename)
