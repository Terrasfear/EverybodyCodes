class Game:
    def __init__(self, columns: list):
        self.columns = columns
        self.round = 0

    def clap_round(self):
        clapper = self.columns[self.round % len(self.columns)].pop(0)
        clapping_column = self.columns[(self.round + 1) % len(self.columns)]

        clapper_mod = (clapper - 1) % (2 * len(clapping_column))
        if clapper_mod < len(clapping_column):
            clapping_column.insert(clapper_mod, clapper)
        else:
            clapping_column.insert(2 * len(clapping_column) - clapper_mod, clapper)

        self.round += 1

    def front_row(self):
        return "".join([str(column[0]) for column in self.columns])

    def print(self):
        max_column_length = max([len(column) for column in self.columns])

        for position in range(max_column_length):
            for column in self.columns:
                if len(column) <= position:
                    print(" ", end=" ")
                else:
                    print(column[position], end=" ")
            print()


for part in [1, 2, 3]:
    with open(f"Input_{part}", 'r') as _file:
        _lines = _file.readlines()

        _num_columns = len(_lines[0].removesuffix("\n").split())
        _columns = [[] for _ in range(_num_columns)]

        for line in _lines:
            knights = line.split()
            for column_idx, knight in enumerate(knights):
                _columns[column_idx].append(int(knight))

    game = Game(_columns)

    if part == 1:
        rounds = 10

        for round_number in range(rounds):
            game.clap_round()

        part_answer = game.front_row()

    elif part == 2 or part == 3:
        front_row_counter = {}

        while (1):
            game.clap_round()
            front_row = game.front_row()

            if front_row in front_row_counter:
                front_row_counter[front_row] += 1
                if front_row_counter[front_row] >= 2024:
                    break
            else:
                front_row_counter[front_row] = 1
        if part == 2:
            part_answer = int(front_row) * game.round
        else: # part == 3
            part_answer = max([int(key) for key in front_row_counter.keys()])
            pass


    print(f"Part {part}: {part_answer}", end="\n\n\n")
