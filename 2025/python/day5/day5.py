import sys


filename = sys.argv[1]


def build_fresh_ing_tree(fresh_ingredients):
    tree_node = {"low": -1, "high": -1, "left": None, "right": None}

    tree = None
    fresh_ingredients.sort()
    for ingredient_range in fresh_ingredients:
        [low, high] = ingredient_range.split("-")
        if tree is None:
            node = tree_node.copy()
            node["low"] = int(low)
            node["high"] = int(high)
            tree = node
            continue

        curr_tree_node = tree
        while True:
            low_compare = -1
            high_compare = -1
            if int(low) > curr_tree_node["high"]:
                low_compare = 1
            elif int(low) <= curr_tree_node["high"] and int(low) > curr_tree_node["low"]:
                low_compare = 0
            elif int(low) <= curr_tree_node["low"]:
                low_compare = -1
            else:
                print("unknown low compare")

            if int(high) > curr_tree_node["high"]:
                high_compare = 1
            elif int(high) <= curr_tree_node["high"] and int(high) > curr_tree_node["low"]:
                high_compare = 0
            elif int(high) <= curr_tree_node["low"]:
                high_compare = -1
            else:
                print("unknown low compare")

            if low_compare == 1:
                if curr_tree_node["right"] is None:
                    node = tree_node.copy()
                    node["low"] = int(low)
                    node["high"] = int(high)
                    curr_tree_node["right"] = node
                    break

                curr_tree_node = curr_tree_node["right"]
            elif high_compare == -1:
                if curr_tree_node["left"] is None:
                    node = tree_node.copy()
                    node["low"] = int(low)
                    node["high"] = int(high)
                    curr_tree_node["left"] = node
                    break

                curr_tree_node = curr_tree_node["left"]
            else:
                if low_compare == -1:
                    curr_tree_node["low"] = int(low)
                if high_compare == 1:
                    curr_tree_node["high"] = int(high)

                break

    # balance tree

    return tree


def balance_tree(tree):
    if tree["left"] is None and tree["right"] is None:
        return tree

    balance_left = balance_tree(tree["left"])
    balance_right = balance_tree(tree["right"])

    if balance_left is not None and balance_left["high"] > tree["low"]:
        tree["low"] = balance_left["low"]
        balance_left["low"] = None
        balance_left["high"] = None

    if balance_right is not None and balance_right["low"] < tree["high"]:
        tree["high"] = balance_left["high"]
        balance_right["low"] = None
        balance_right["right"] = None

    return tree


def cnt_fresh_ingredients(tree, acc):
    if tree is None:
        return acc

    cnt_left = cnt_fresh_ingredients(tree["left"], acc)
    cnt_right = cnt_fresh_ingredients(tree["right"], acc)

    return cnt_left + cnt_right + tree["high"] - tree["low"] + 1


def run(filename):
    with open(filename, "r") as f:
        data = f.read().strip().split('\n\n')

    fresh_ingredients = data[0].split("\n")
    avail_ingredients = data[1].split("\n")

    num_avail_fresh = 0
    fresh_tree = build_fresh_ing_tree(fresh_ingredients)
    for ingredient in avail_ingredients:
        for ingredient_range in fresh_ingredients:
            [low, high] = ingredient_range.split("-")
            if low is None or high is None:
                continue
            if int(ingredient) >= int(low) and int(ingredient) <= int(high):
                num_avail_fresh += 1
                break

    total_fresh = cnt_fresh_ingredients(fresh_tree, 0)

    print(f"Num Fresh Ingredients: {num_avail_fresh}")
    print(f"Total Fresh Ingredients: {total_fresh}")


run(filename)
