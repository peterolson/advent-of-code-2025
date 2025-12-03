with open("input/2.txt", "r") as f:
    line = f.readline().strip()

ranges = line.split(",")
ranges = [r.split("-") for r in ranges]
ranges = [(int(left), int(right)) for left, right in ranges]


def is_invalid(num: str, divisor: int = 2) -> bool:
    if len(num) % divisor != 0:
        return False
    parts = [
        num[i : i + len(num) // divisor]
        for i in range(0, len(num), len(num) // divisor)
    ]
    return all(part == parts[0] for part in parts)


invalid_sum = 0
for left, right in ranges:
    invalids = [num for num in range(left, right + 1) if is_invalid(str(num))]
    invalid_sum += sum(invalids)

print(invalid_sum)


def is_invalid_v2(num: str) -> bool:
    for divisor in range(2, len(num) + 1):
        if is_invalid(num, divisor):
            return True
    return False


invalid_sum_v2 = 0
for left, right in ranges:
    invalids = [num for num in range(left, right + 1) if is_invalid_v2(str(num))]
    invalid_sum_v2 += sum(invalids)
print(invalid_sum_v2)
