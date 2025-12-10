with open("input/9.txt", "r") as f:
    lines = f.readlines()

lines = [line.rstrip("\n").split(",") for line in lines]
coords = [(int(x), int(y)) for x, y in lines]


def get_rect_area(p1: tuple[int, int], p2: tuple[int, int]) -> int:
    width = abs(p1[0] - p2[0]) + 1
    height = abs(p1[1] - p2[1]) + 1
    return width * height


pairwise_areas: dict[tuple[int, int], int] = {}
for i in range(len(coords)):
    for j in range(i + 1, len(coords)):
        pairwise_areas[(i, j)] = get_rect_area(coords[i], coords[j])

max_area = max(pairwise_areas.values())
print(max_area)
