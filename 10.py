import itertools

with open("input/10.txt", "r") as f:
    lines = f.readlines()


def parse_line(line: str) -> tuple[list[int], list[list[int]], list[int]]:
    parts = line.rstrip("\n").split(" ")
    target_indicators = parts[0][1:-1]
    list_indicators: list[int] = []
    for i in range(len(target_indicators)):
        if target_indicators[i] == "#":
            list_indicators.append(i)
    joltages = parts[-1][1:-1].split(",")
    lists = parts[1:-1]
    lists = [lst[1:-1].split(",") for lst in lists]
    lists_int = [[int(x) for x in lst] for lst in lists]
    joltages_int = [int(x) for x in joltages]
    return (list_indicators, lists_int, joltages_int)


def to_int(indices: list[int]) -> int:
    result = 0
    for index in indices:
        result += 1 << index
    return result


def xor(list: tuple[int, ...]) -> int:
    result = 0
    for item in list:
        result ^= item
    return result


def find_solution(target: int, buttons: list[int]):
    n = len(buttons)
    for r in range(1, n + 1):
        for combo in itertools.combinations(buttons, r):
            if xor(combo) == target:
                return combo
    return []


lines_parsed = [parse_line(line) for line in lines]
presses = 0
for target, lists, joltages in lines_parsed:
    solution = find_solution(to_int(target), [to_int(lst) for lst in lists])
    presses += len(solution)

print(presses)

import z3

presses = 0
for target, lists, joltages in lines_parsed:
    opt = z3.Optimize()
    vars = []
    for i in range(len(lists)):
        var = z3.Int(f"var_{i}")
        vars.append(var)
        opt.add(var >= 0)

    for j in range(len(joltages)):
        joltage = joltages[j]
        contributing_vars = [vars[i] for i in range(len(lists)) if j in lists[i]]
        opt.add(z3.Sum(contributing_vars) == joltage)

    opt.minimize(z3.Sum(vars))
    if opt.check() == z3.sat:
        model = opt.model()
        presses += sum(model.evaluate(var).as_long() for var in vars)

print(presses)
