def printPowerSet(set, set_size):
    power_set_size = 2**set_size
    outer = 0
    inner = 0
    for outer in range(0, power_set_size):
        subset = ""
        for inner in range(0, set_size):
            if(outer & (1 << inner)) > 0:
                subset += str(set[inner]) + " "
        print(f"[{subset}]")
set = [1, 2, 3]
printPowerSet(set, len(set))