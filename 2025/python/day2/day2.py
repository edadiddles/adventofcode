import sys

filename = sys.argv[1]


with open(filename, "r") as f:
    data = f.read().split(",")

invalid_prod_nums = []
for datum in data:
    [low, high] = datum.split("-")
    print(f"{low} - {high}")
    while int(low) <= int(high):
        if low[:len(low)//2] == low[len(low)//2:]:
            print(f"duplicated product number: {low}")
            invalid_prod_nums.append(int(low))
        low = str(int(low)+1)

print("sum of invalid product numbers:", sum(invalid_prod_nums))
