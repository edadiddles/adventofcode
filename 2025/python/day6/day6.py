import sys

filename = sys.argv[1]


def run(filename):
    with open(filename, "r") as f:
        data = f.read().strip().split("\n")

    operations = data[-1]
    total_chars = len(operations)
    operations = [op for op in operations if op != " "]
    n = total_chars//len(operations)+1

    total = []
    for op in operations:
        match op:
            case "+":
                total.append(0)
            case "*":
                total.append(1)

    for datum in data[:-1]:
        curr_row = []
        curr_val = ""
        for c in datum:
            if c == " " and curr_val != "":
                curr_row.append(int(curr_val))
                curr_val = ""
            elif c != " ":
                curr_val += c

        if curr_val != "":
            curr_row.append(int(curr_val))

        for idx, val in enumerate(curr_row):
            # print(f"{idx}, {val} -- {operations[idx]}")
            match operations[idx]:
                case "+":
                    total[idx] += val
                case "*":
                    total[idx] *= val

    # print(total)
    print(f"Total: {sum(total)}")


run(filename)
