import sys


filename = sys.argv[1]


def run(filename):
    with open(filename, "r") as f:
        data = f.read().strip().split('\n\n')

    fresh_ingredients = data[0].split("\n")
    avail_ingredients = data[1].split("\n")

    num_fresh = 0
    for ingredient in avail_ingredients:
        for ingredient_range in fresh_ingredients:
            [low, high] = ingredient_range.split("-")
            if int(ingredient) >= int(low) and int(ingredient) <= int(high):
                num_fresh += 1
                break

    print(f"Num Fresh Ingredients: {num_fresh}")


run(filename)
