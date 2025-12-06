def rotate(position: int, rotation: str) -> tuple:
    direction = rotation[0]
    ticks = int(rotation[1:])

    if direction == "L":
        end = (position - ticks) % 100
        zeros = (
            (position - ticks - 100) // -100
            if position != 0
            else (position - ticks) // -100
        )
    else:
        end = (position + ticks) % 100
        zeros = (position + ticks) // 100

    return end, zeros


def load_file(file_name: str) -> str:
    with open(file_name, "r") as f:
        return f.read()


def main():
    instr_data = load_file("day_1/puzzle.txt")
    rotations = instr_data.split("\n")

    position = 50

    zero_lands = 0
    zero_passes = 0

    for rotation in rotations:
        position, zeros = rotate(position, rotation)

        if position == 0:
            zero_lands += 1

        zero_passes += zeros

    print(position, zero_lands, zero_passes)


if __name__ == "__main__":
    main()
