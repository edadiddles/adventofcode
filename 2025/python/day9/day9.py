import sys

filename = sys.argv[1]


def run(filename):
    with open(filename, "r") as f:
        data = f.read().strip().split("\n")

    max_area = 0
    coord_list = []
    for row in data:
        coords = row.strip().split(",")
        coord_list.append([int(c) for c in coords])

    for coord1 in coord_list[:-1]:
        for coord2 in coord_list[1:]:
            width = coord2[0]-coord1[0]
            if width < 0:
                width *= -1
            width += 1

            height = coord2[1]-coord1[1]
            if height < 0:
                height *= -1
            height += 1
            area = width*height

            # print(f"Coords: ({coord1[0]}, {coord1[1]}) -- ({coord2[0]}, {coord2[1]}) == {area}")
            if area > max_area:
                max_area = area

    print(f"Largest Area: {max_area}")


run(filename)
