def dig(height_map: dict, dig_candidates: list, neighbour_directions: list):
    next_dig_candidates = []

    for dig_candidate in dig_candidates:
        candidate_value = height_map[dig_candidate]

        neighbours = [tuple(map(sum, zip(dig_candidate, direction))) for direction in neighbour_directions]
        neighbour_values = [0 if neighbour not in height_map else height_map[neighbour] for neighbour in neighbours]

        if min(neighbour_values) >= candidate_value and max(neighbour_values) <= candidate_value + 1:
            height_map[dig_candidate] += 1
            next_dig_candidates.append(dig_candidate)

    if not next_dig_candidates:
        return
    else:
        dig(height_map, next_dig_candidates, neighbour_directions)


def print_height_map(height_map):
    for y in range(height):
        for x in range(width):
            if (x, y) not in height_map:
                print(".", end="")
            else:
                print(height_map[(x, y)], end="")
        print()


for part in [1, 2, 3]:
    with open(f"Input_{part}", 'r') as _file:
        _lines = _file.readlines()
        width = len(_lines[0].removesuffix("\n"))
        height = len(_lines)

        height_map_ = {}

        for y, line in enumerate(_lines):
            for x, char in enumerate(line.removesuffix("\n")):
                if char == "#":
                    height_map_[(x, y)] = 1

    if part == 3:
        neighbour_directions_ = [(1, 0),(0, 1), (-1, 0), (0, -1), (1,1), (1,-1), (-1, -1), (-1, 1)]
    else:
        neighbour_directions_ = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    dig(height_map_, list(height_map_.keys()), neighbour_directions_)

    print_height_map(height_map_)

    print(f"Part {part}: {sum(height_map_.values())}", end="\n\n\n")
