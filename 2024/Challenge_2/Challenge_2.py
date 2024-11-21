part = 1
with open(f"Input_{part}",'r') as _file:
    _lines = _file.readlines()

    runes = _lines[0].removeprefix("WORDS:").removesuffix("\n").split(",")
    inscription = _lines[2].removesuffix("\n")

rune_count = 0
for rune in runes:
    rune_count += inscription.count(rune)

print(f"Part {part}: {rune_count}")


part = 2
with open(f"Input_{part}",'r') as _file:
    _lines = _file.readlines()

    runes = set(_lines[0].removeprefix("WORDS:").removesuffix("\n").split(","))
    runes.update([rune[::-1] for rune in runes])
    inscription = [line.removesuffix("\n") for line in _lines[2:]]

rune_count = 0
for line in inscription:
    symbol_set = [False for _ in range(len(line))]

    for rune in runes:
        line_to_check = line
        rune_length = len(rune)
        past_index = 0
        while (rune_index := line_to_check.find(rune)) != -1:
            for i in range(past_index + rune_index, past_index + rune_index+rune_length):
                symbol_set[i] = True
            line_to_check = line_to_check[rune_index+1:]
            past_index += rune_index+1

    rune_count += sum(symbol_set)

print(f"Part {part}: {rune_count}")


def print_line(line, bold_set):
    for i, char in enumerate(line):
        if bold_set[i]:
            print(f"\033[36m{char}\033[0m",end="")
        else:
            print(f"{char}",end="")
    print()

part = 3
with open(f"Input_{part}",'r') as _file:
    _lines = _file.readlines()

    runes = set(_lines[0].removeprefix("WORDS:").removesuffix("\n").split(","))
    runes.update([rune[::-1] for rune in runes])
    inscription = [line.removesuffix("\n") for line in _lines[2:]]
    num_lines = len(inscription)
    line_length = len(inscription[0])

rune_count = 0
symbol_set = [[False for _ in range(line_length)] for _ in range(num_lines)]

# row search
for line_index, line in enumerate(inscription):
    for rune in runes:
        rune_length = len(rune)
        line_to_check = line + line[:rune_length-1]
        past_index = 0
        while (rune_index := line_to_check.find(rune)) != -1:
            for i in range(past_index + rune_index, past_index + rune_index+rune_length):
                if i >= line_length:
                    i -= line_length

                symbol_set[line_index][i] = True
            line_to_check = line_to_check[rune_index+1:]
            past_index += rune_index+1

# column search
for column_index in range(line_length):
    column = "".join([line[column_index] for line in inscription])
    for rune in runes:
        rune_length = len(rune)
        column_to_check = column
        past_index = 0
        while (rune_index := column_to_check.find(rune)) != -1:
            for i in range(past_index + rune_index, past_index + rune_index+rune_length):
                if i >= num_lines:
                    i -= num_lines

                symbol_set[i][column_index] = True
            column_to_check = column_to_check[rune_index+1:]
            past_index += rune_index+1


for line_index, line in enumerate(inscription):
    print_line(line, symbol_set[line_index])
    rune_count += sum(symbol_set[line_index])

print(f"Part {part}: {rune_count}")