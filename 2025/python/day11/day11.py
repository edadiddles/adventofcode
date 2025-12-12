import sys


filename = sys.argv[1]


def walk_graph(graph, input, acc):
    if input == "out":
        return 1

    accs = []
    for val in graph[input]:
        accs.append(walk_graph(graph, val, acc))

    return sum(accs)


def run(filename):
    with open(filename, "r") as f:
        data = f.read().strip().split("\n")

    map = {}
    for datum in data:
        (k, v) = datum.strip().split(": ")
        map[k] = v.strip().split(" ")

    num_paths = walk_graph(map, "you", 0)
    print(f"Total Paths: {num_paths}")


run(filename)
