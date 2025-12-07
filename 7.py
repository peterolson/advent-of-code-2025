with open("input/7.txt", "r") as f:
    lines = f.readlines()

lines = [line.rstrip("\n") for line in lines]

new_lines: list[str] = []
splits = 0
for i, line in enumerate(lines):
    if i == 0:
        new_lines.append(line)
        continue
    new_line = ["."] * len(line)
    for j, char in enumerate(line):
        above_char = new_lines[i - 1][j]
        if char == "^" and above_char == "|":
            splits += 1
            new_line[j] = "^"
            if j > 0 and new_line[j - 1] == ".":
                new_line[j - 1] = "|"
            if j < len(line) - 1 and new_line[j + 1] == ".":
                new_line[j + 1] = "|"
        elif char == "." and above_char in ["|", "S"]:
            new_line[j] = "|"
    new_lines.append("".join(new_line))

print(splits)

new_lines: list[str] = []
possibility_counts: list[list[int]] = []

for i, line in enumerate(lines):
    if i == 0:
        new_lines.append(line)
        possibilities = [0] * len(line)
        possibilities[line.index("S")] = 1
        possibility_counts.append(possibilities)
        continue
    possibilities = [0] * len(line)
    new_line = ["."] * len(line)
    for j, char in enumerate(line):
        above_char = new_lines[i - 1][j]
        if char == "^" and above_char == "|":
            new_line[j] = "^"
            if j > 0 and new_line[j - 1] in [".", "|"]:
                new_line[j - 1] = "|"
                possibilities[j - 1] += possibility_counts[i - 1][j]
            if j < len(line) - 1 and new_line[j + 1] in [".", "|"]:
                new_line[j + 1] = "|"
                possibilities[j + 1] += possibility_counts[i - 1][j]
        elif char == "." and above_char in ["|", "S"]:
            new_line[j] = "|"
            possibilities[j] += possibility_counts[i - 1][j]
    new_lines.append("".join(new_line))
    possibility_counts.append(possibilities)

print(sum(possibility_counts[-1]))
