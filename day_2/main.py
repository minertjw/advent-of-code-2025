from typing import List


def load_file(file_name: str) -> str:
    with open(file_name, "r") as f:
        return f.read()


def front(bound: str):
    return bound[0 : len(bound) // 2]


def check_range(id_range: str) -> List[int]:
    bounds = id_range.split("-")
    lower: str = bounds[0]
    upper: str = bounds[1]

    # Fast forward bounds to even digits
    if len(lower) % 2 != 0:
        lower = str(1 * (10 ** len(lower)))

    if len(upper) % 2 != 0:
        upper = str(1 * (10 ** (len(upper) - 1)) - 1)

    if int(lower) > int(upper):
        return []

    # Fast forward bounds to closest repeated sequence
    first = 2 * front(lower)
    if int(first) >= int(lower):
        lower = first
    else:
        lower = 2 * str(int(front(lower)) + 1)

    last = 2 * front(upper)
    if int(last) <= int(upper):
        upper = last
    else:
        upper = 2 * str(int(front(upper)) - 1)

    if int(lower) > int(upper):
        return []

    if int(upper) == int(lower):
        return [int(lower)]

    # Use guaranteed number of invalids between bounds to build array of invalids
    lower_front = int(front(lower))
    upper_front = int(front(upper))
    invalid_count = upper_front - lower_front + 1

    invalid_ids = []

    for i in range(invalid_count):
        invalid_ids.append(int(2 * str(lower_front + i)))

    return invalid_ids


def main():
    puzzle = load_file("day_2/puzzle.txt")

    id_ranges = puzzle.split(",")
    invalid_ids = []

    for id_range in id_ranges:
        invalid_ids.extend(check_range(id_range))

    print(sum(invalid_ids))


if __name__ == "__main__":
    main()
