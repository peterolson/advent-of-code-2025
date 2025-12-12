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


def point_on_edge(point: tuple[int, int], polygon: list[tuple[int, int]]) -> bool:
    x, y = point
    n = len(polygon)
    for i in range(n):
        p1x, p1y = polygon[i]
        p2x, p2y = polygon[(i + 1) % n]
        if p1x == p2x:  # vertical edge
            if x == p1x and min(p1y, p2y) <= y <= max(p1y, p2y):
                return True
        elif p1y == p2y:  # horizontal edge
            if y == p1y and min(p1x, p2x) <= x <= max(p1x, p2x):
                return True
    return False


def point_inside_polygon(
    point: tuple[int, int], polygon: list[tuple[int, int]]
) -> bool:
    if point_on_edge(point, polygon):
        return True
    # Ray casting algorithm
    x, y = point
    xinters = 0
    inside = False
    n = len(polygon)
    p1x, p1y = polygon[0]
    for i in range(n + 1):
        p2x, p2y = polygon[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside


def polygon_inside(
    polygon1: list[tuple[int, int]], polygon2: list[tuple[int, int]]
) -> bool:
    return all(point_inside_polygon(p, polygon2) for p in polygon1) and all(
        not point_inside_polygon(p, polygon1) or point_on_edge(p, polygon1)
        for p in polygon2
    )


def rect_to_polygon(p1: tuple[int, int], p2: tuple[int, int]) -> list[tuple[int, int]]:
    # if they are on the same x or y coordinate, return p1, p2 only
    if p1[0] == p2[0] or p1[1] == p2[1]:
        return [p1, p2]
    return [
        (min(p1[0], p2[0]), min(p1[1], p2[1])),
        (max(p1[0], p2[0]), min(p1[1], p2[1])),
        (max(p1[0], p2[0]), max(p1[1], p2[1])),
        (min(p1[0], p2[0]), max(p1[1], p2[1])),
    ]


pairwise_areas_inside_loop: dict[tuple[int, int], int] = {}
len_pairwise = len(pairwise_areas)
item_count = 0
for (i, j), area in pairwise_areas.items():
    item_count += 1
    if item_count % 1000 == 0:
        print(f"Checking pair {item_count} of {len_pairwise}")
    poly1 = rect_to_polygon(coords[i], coords[j])
    if not polygon_inside(poly1, coords):
        continue
    pairwise_areas_inside_loop[(i, j)] = area

max_area_inside_loop = max(pairwise_areas_inside_loop.values())
print(max_area_inside_loop)
