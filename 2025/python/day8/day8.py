import sys

filename = sys.argv[1]


def calc_dist(node1, node2):
    (x1, y1, z1) = node1["coords"]
    (x2, y2, z2) = node2["coords"]

    return (x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2


def find_distances(nodes):
    distances = []
    for idx1, node1 in enumerate(nodes[0:-1]):
        for idx2, node2 in enumerate(nodes[idx1+1:]):
            distances.append({
                "dist": calc_dist(node1, node2),
                "node1": node1,
                "node2": node2
            })

    return sorted(distances, key=lambda d: d["dist"])


def determine_circuit_sizes(nodes, distances):
    circuit_sizes = []
    for node in nodes:
        circuit_size = count_nodes(node, distances)
        node["visited"] = True
        if circuit_size > 0:
            circuit_sizes.append(circuit_size)

    return circuit_sizes


def count_nodes(node, distances):
    if "visited" in node:
        return 0

    size = 1
    for d in distances:
        if node["id"] == d["node1"]["id"]:
            node["visited"] = True
            size += count_nodes(d["node2"], distances)
        elif node["id"] == d["node2"]["id"]:
            node["visited"] = True
            size += count_nodes(d["node1"], distances)

    return size


def run(filename):
    product = 1
    with open(filename, "r") as f:
        data = f.read().strip().split("\n")

    nodes = []
    for idx, row in enumerate(data):
        coords = [int(coord) for coord in row.split(",")]
        nodes.append({"id": idx, "coords": coords, "edges": []})

    distances = find_distances(nodes)
    circuit_sizes = determine_circuit_sizes(nodes, distances[0:10])
    print(f"Num Junctions: {sum(circuit_sizes)}")
    print(f"Num Circuits: {len(circuit_sizes)}")
    print(f"Circuit Sizes: {sorted(circuit_sizes, reverse=True)}")
    for size in sorted(circuit_sizes, reverse=True)[0:3]:
        product *= size
    print(f"Product of Circuit Sizes: {product}")


run(filename)
