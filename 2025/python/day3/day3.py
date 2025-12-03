import sys


def find_max_value(datum, from_idx, to_idx):
    idx = from_idx+1

    max_idx = idx
    while idx <= to_idx:
        if datum[idx] > datum[max_idx]:
            max_idx = idx

        idx += 1

    return max_idx


def run(filename, num_batteries):

    with open(filename, "r") as f:
        data = f.read().strip().split("\n")

    joltages = []
    for datum in data:

        selected_indices = []
        while len(selected_indices) < num_batteries:
            from_idx = selected_indices[-1] if len(selected_indices) > 0 else -1
            to_idx = len(datum) - num_batteries + len(selected_indices)
            selected_indices.append(find_max_value(datum, from_idx, to_idx))

        str_val = "".join([str(datum[idx]) for idx in selected_indices])
        joltages.append(int(str_val))

    print(f"Output Joltage: {sum(joltages)}")


filename = sys.argv[1]
num_batteries = int(sys.argv[2])

run(filename, num_batteries)
