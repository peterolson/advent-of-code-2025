with open("input/1.txt", "r") as f:
    lines = f.readlines()

start_pos = 50

zero_count = 0
for line in lines:
    dir = line[0]
    steps = int(line[1:])

    quotient, steps = divmod(steps, 100)
    zero_count += quotient

    init_pos = start_pos

    if dir == "L":
        start_pos -= steps

    elif dir == "R":
        start_pos += steps

    if start_pos == 0:
        if init_pos != 0:
            zero_count += 1
    elif start_pos < 0:
        start_pos += 100
        if init_pos != 0:
            zero_count += 1
    elif start_pos >= 100:
        start_pos -= 100
        if init_pos != 0:
            zero_count += 1

print(zero_count)
