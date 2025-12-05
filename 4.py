with open("input/4.txt", "r") as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

grid = {}
rows = len(lines)
cols = len(lines[0])
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        grid[(x, y)] = char


def get_accessible_positions(grid):
    accessible = set()
    for y in range(rows):
        for x in range(cols):
            char = grid[(x, y)]
            if char != "@":
                continue

            adjacent_roll_count = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    adjacent = grid.get((x + dx, y + dy))
                    if adjacent == "@":
                        adjacent_roll_count += 1

            if adjacent_roll_count < 4:
                accessible.add((x, y))
    return accessible


accessible = get_accessible_positions(grid)
total_removed = len(accessible)

print(total_removed)

while len(accessible) > 0:
    for coord in accessible:
        grid[coord] = "."

    accessible = get_accessible_positions(grid)
    total_removed += len(accessible)

print(total_removed)
