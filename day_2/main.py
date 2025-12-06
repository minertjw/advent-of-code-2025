from typing import List


def load_file(file_name: str) -> str:
    with open(file_name, "r") as f:
        return f.read()


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
    first = 2 * lower[0 : len(lower) // 2]
    if int(first) >= int(lower):
        lower = first
    else:
        lower = 2 * str(int(lower[0 : len(lower) // 2]) + 1)

    last = 2 * upper[0 : len(upper) // 2]
    if int(last) <= int(upper):
        upper = last
    else:
        upper = 2 * str(int(upper[0 : len(upper) // 2]) - 1)

    if int(lower) > int(upper):
        return []

    if int(upper) == int(lower):
        return [int(upper)]

    # Increment on 
    increment = 1 * 10 ** (len(lower) // 2)
    invalid_ids = []

    while int(lower) < int(upper):
        if lower[0:len(lower)//2] == lower[len(lower)//2:]:
            invalid_ids.append(int(lower))
        
        lower = str(int(lower) + increment)
        lower = 2 * lower[0 : len(lower) // 2]
    
    if upper[0:len(upper)//2] == upper[len(upper)//2:]:
        invalid_ids.append(int(upper))
    
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
