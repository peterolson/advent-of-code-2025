with open("input/6.txt", "r") as f:
    input_lines = f.readlines()

lines = [line.strip().split() for line in input_lines]
numbers = lines[0:-1]
operations = lines[-1]


def multiply(nums: list[str]) -> int:
    result = 1
    for num in nums:
        result *= int(num)
    return result


def add(nums: list[str]) -> int:
    result = 0
    for num in nums:
        result += int(num)
    return result


total = 0
for i, operation in enumerate(operations):
    nums = [n[i] for n in numbers]
    res = 0
    if operation == "+":
        res = add(nums)
    elif operation == "*":
        res = multiply(nums)
    total += res

print(total)

operations_line = input_lines[-1]
widths: list[int] = []
width = 0
for i, char in enumerate(operations_line):
    if i == 0:
        continue
    width += 1
    if char == "+" or char == "*":
        widths.append(width)
        width = 0

widths.append(width + 1)

raw_texts = []
for line in input_lines[:-1]:
    start = 0
    parts: list[str] = []
    for w in widths:
        parts.append(line[start : start + w])
        start += w
    raw_texts.append(parts)


def parse_operands(operands: list[str]) -> list[str]:
    result: list[str] = []
    i = len(operands[0]) - 1
    while i >= 0:
        num_str = ""
        for op in operands:
            if op[i].isdigit():
                num_str = num_str + op[i]
        if num_str != "":
            result.append(num_str)
        i -= 1
    return result


total = 0
for i, operation in enumerate(operations):
    operands = [r[i] for r in raw_texts]
    nums = parse_operands(operands)
    if operation == "+":
        total += add(nums)
    elif operation == "*":
        total += multiply(nums)

print(total)
