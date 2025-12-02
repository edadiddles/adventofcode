import sys

filename = sys.argv[1]


with open(filename, "r") as f:
    data = f.read().split(",")

invalid_prod_nums = []
for datum in data:
    [low, high] = datum.split("-")
    print(f"{low} - {high}")
    while int(low) <= int(high):
        l = 1
        while l <= len(low)//2:
            s = len(low)//l
            if s != len(low)/l:
                l += 1
                continue

            is_equal = True
            for k in range(1, s):
                if low[(k-1)*l:k*l] != low[k*l:(k+1)*l]:
                    is_equal = False
                    break

            if is_equal:
                print(f"duplicated product number: {low}")
                invalid_prod_nums.append(int(low))
                break

            l += 1
        low = str(int(low)+1)

print("sum of invalid product numbers:", sum(invalid_prod_nums))
