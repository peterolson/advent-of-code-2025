with open("input/3.txt", "r") as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]


def get_joltage(bank: str) -> int:
    highest = max(int(j) for j in bank[:-1])
    index_of_highest = bank.index(str(highest))
    remainder = bank[index_of_highest + 1 :]
    next_highest = max(int(j) for j in remainder)
    return int(str(highest) + str(next_highest))


total_joltage = sum(get_joltage(line) for line in lines)
print(total_joltage)


def get_joltage_v2(bank: str, length: int) -> int:
    highest = max(int(j) for j in bank[: -length + 1])
    joltage_str = str(highest)
    while len(joltage_str) < length:
        index_of_highest = bank.index(str(highest))
        remainder = bank[index_of_highest + 1 :]
        remaining_length = length - len(joltage_str)
        remainder_to_search = remainder[: len(remainder) - remaining_length + 1]
        next_highest = max(int(j) for j in remainder_to_search)
        joltage_str += str(next_highest)
        highest = next_highest
        bank = remainder
    return int(joltage_str)


print(sum(get_joltage_v2(line, 12) for line in lines))
