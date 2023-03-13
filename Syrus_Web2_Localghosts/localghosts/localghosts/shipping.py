# kgs for example
# available_space = free_weight
used_weight = 0
flag = False

# free_weight=100


def space(truck_capacity, items):
    free_weight = truck_capacity
    # while free_weight != 0:
    for free_weight in range(truck_capacity):
        if free_weight <= 0:
            return free_weight
            # break
        used_weight = sum(items)
        free_weight = truck_capacity - used_weight
    return free_weight

items = [30, 40, 30]
print(space(50, items))