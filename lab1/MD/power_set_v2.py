def power_set(set):
    if len(set) == 0:
        return [[]]
    else:
        subsets = []
        for subset in power_set(set[1:]):
            subsets += [subset]
            subsets += [[set[0]] + subset]
        return subsets

def empty_power_set(emty_set):
    return [[], [[]]]

print(power_set([1,2,[3]])) 
#print(empty_power_set([]))