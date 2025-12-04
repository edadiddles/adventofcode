import sys

filename = sys.argv[1]


def run(filename):
    with open(filename, "r") as f:
        rows = f.read().strip().split("\n")

    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    num_access = 0
    output = []
    for j, row in enumerate(rows):
        output_row = []
        for i, col in enumerate(row):
            output_row.append(col)
            num_adj = 0
            if col == "@":
                for dir in dirs:
                    x, y = dir
                    if x+j >= 0 and x+j < len(row) and y+i >= 0 and y+i < len(rows) and rows[x+j][y+i] == "@":
                        num_adj += 1

                if num_adj < 4:
                    output_row[-1] = "x"
                    num_access += 1

        output.append("".join(output_row))

    print(f"Output: {num_access}")
    print("\n".join(output))


run(filename)
