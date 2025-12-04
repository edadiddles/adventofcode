import sys
from time import sleep

filename = sys.argv[1]


def run(filename):
    with open(filename, "r") as f:
        rows = f.read().strip().split("\n")

    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    total_access = 0
    output = []
    input = rows
    num_access = 10  # hack to get into loop
    while num_access > 0:
        num_access = 0
        for j, row in enumerate(input):
            #print(row)
            output_row = []
            for i, col in enumerate(row):
                output_row.append(col)
                num_adj = 0
                if col == "@":
                    for dir in dirs:
                        x, y = dir
                        if x+j >= 0 and x+j < len(row) and y+i >= 0 and y+i < len(input) and input[x+j][y+i] == "@":
                            num_adj += 1

                    if num_adj < 4:
                        output_row[-1] = "x"
                        num_access += 1

            output.append("".join(output_row))

        total_access += num_access
        input = output
        output = []
        #print("----------")

    print(f"Output: {total_access}")


run(filename)
