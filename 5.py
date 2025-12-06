with open("input/5.txt", "r") as f:
    lines = f.read()

ranges, ingredients = lines.split("\n\n")
ranges = ranges.strip().split("\n")
ranges = [r.split("-") for r in ranges]
ranges = [(int(start), int(end)) for start, end in ranges]

ingredients = ingredients.strip().split("\n")
ingredients = [int(i) for i in ingredients]


def is_fresh(ingredient: int, ranges: list[tuple[int, int]]) -> bool:
    for start, end in ranges:
        if start <= ingredient <= end:
            return True
    return False


fresh_ingredients = [i for i in ingredients if is_fresh(i, ranges)]
print(len(fresh_ingredients))


def ranges_overlap(r1: tuple[int, int], r2: tuple[int, int]) -> bool:
    return not (r1[1] < r2[0] or r2[1] < r1[0])


def merge_ranges(r1: tuple[int, int], r2: tuple[int, int]) -> tuple[int, int]:
    return (min(r1[0], r2[0]), max(r1[1], r2[1]))


def merge_all_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    merged = []
    for r in sorted(ranges):
        if not merged or not ranges_overlap(merged[-1], r):
            merged.append(r)
        else:
            merged[-1] = merge_ranges(merged[-1], r)
    return merged


def get_length(ranges: list[tuple[int, int]]) -> int:
    total_length = 0
    for start, end in ranges:
        total_length += end - start + 1
    return total_length


print(get_length(merge_all_ranges(ranges)))
