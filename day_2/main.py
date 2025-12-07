from typing import List, Union

factors_lookup = {}


def load_file(file_name: str) -> str:
    with open(file_name, "r") as f:
        return f.read()


def front(bound: str, length: Union[None, int] = None) -> str:
    if length is None:
        length = len(bound) // 2
    return bound[0:length]


def get_factors(num_length: int) -> List[int]:
    global factors_lookup

    if factors_lookup.get(num_length, None) is not None:
        return factors_lookup[num_length]
    else:
        factors = []
        for i in range(1, num_length):
            if num_length % i == 0:
                factors.append(i)
        factors_lookup[num_length] = factors
        return factors


def get_limits(factors: List[int], bound: str) -> List[int]:
    limits = []

    for factor in factors:
        lower_front = front(bound, factor)
        lower_repeat = lower_front * (len(bound) // factor)
        limits.append(int(lower_repeat))

    return limits


def check_range(id_range: str) -> List[int]:
    bounds = id_range.split("-")
    lower: str = bounds[0]
    upper: str = bounds[1]

    # Filter single digit edge case
    if len(lower) == 1 and len(upper) == 1:
        return []

    # Split into different bounding regions if they do not have the same number of digits
    invalid_ids = []
    if len(lower) != len(upper):
        different = True
    else:
        different = False

    if different:
        for i in range(len(lower), len(upper) + 1):
            split_lower = lower if i == len(lower) else str(1 * (10 ** (i - 1)))
            split_upper = upper if i == len(upper) else str(1 * (10 ** (i)) - 1)
            invalid_ids.extend(check_range(f"{split_lower}-{split_upper}"))
        return invalid_ids

    factors = get_factors(len(lower))

    lower_temp = lower
    while True:
        lower_limits = get_limits(factors, lower_temp)
        lower_limits = [limit for limit in lower_limits if int(limit) >= int(lower)]
        lowest_limit = min(lower_limits, default=-1)
        if lowest_limit >= int(lower):
            break
        else:
            lower_temp = (len(lower) // max(factors)) * str(
                int(front(lower_temp, max(factors))) + 1
            )

    upper_temp = upper
    while True:
        upper_limits = get_limits(factors, upper_temp)
        upper_limits = [limit for limit in upper_limits if int(limit) <= int(upper)]
        highest_limit = max(upper_limits, default=-1)
        if highest_limit <= int(upper) and highest_limit != -1:
            break
        else:
            upper_temp = (len(upper) // max(factors)) * str(
                int(front(upper_temp, max(factors))) - 1
            )

    print(bounds)
    print(f"['{lowest_limit}', '{highest_limit}']\n")

    # Filter edge cases
    if int(lower) > int(highest_limit):
        return []
    elif int(upper) < int(lowest_limit):
        return []
    elif lowest_limit == highest_limit:  # type: ignore
        return [int(lowest_limit)]

    # Do the work
    invalid_ids_index = {}
    for factor in factors:
        lower_front = int(front(str(lowest_limit), factor))
        upper_front = int(front(str(highest_limit), factor))
        invalid_count = upper_front - lower_front + 1

        for i in range(invalid_count):
            latest = int(len(lower) // factor * str(lower_front + i))
            if invalid_ids_index.get(str(latest), None) is None and latest <= int(
                upper
            ):
                invalid_ids.append(latest)
                invalid_ids_index[latest] = True

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
