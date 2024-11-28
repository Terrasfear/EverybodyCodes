class Race:
    def __init__(self):
        self.plans = []
        self.racers = []
        self.energies = []
        self.scores = []
        self.track = []
        self.segments_finished = 0
        self.num_racers = 0

    def addRacer(self, plan):
        self.racers.append(plan[0])
        self.plans.append(plan[1:])
        self.energies.append(10)
        self.scores.append(0)
        self.num_racers += 1

    def addTrack(self, track_description):
        if len(track_description) == 1:  # unlooped track
            self.track = list(track_description[0])
        else:
            track_width = len(track_description[0])
            track_height = len(track_description)
            x_old = 0
            y_old = 0
            x = 1
            y = 0
            track = track_description[y][x]
            while (track[-1] != "S"):
                options = [{"x": x + direction[0], "y": y + direction[1]} for direction in
                           [(1, 0), (0, 1), (-1, 0), (0, -1)]]
                options = [option for option in options
                           if (0 <= option["y"] < track_height and 0 <= option["x"] < len(
                        track_description[option["y"]]))]  # filter out of bounds
                options = [option for option in options
                           if track_description[option["y"]][option["x"]] != " "]  # filter on path
                options = [option for option in options
                           if not (option["x"] == x_old and option["y"] == y_old)]  # filter no double backing

                if len(options) != 1:
                    raise Exception

                x_old = x
                y_old = y
                x = options[0]["x"]
                y = options[0]["y"]

                track += track_description[y][x]

            self.track = list(track)

        if self.track[0] == "S" and len(self.track) != 1:
            self.track.append(self.track.pop(0))

    def runSegment(self, track):
        if track == "S" or track == "=":
            for racer_idx, plan in enumerate(self.plans):
                action = plan[self.segments_finished % len(plan)]
                if action == "+":
                    self.energies[racer_idx] += 1
                elif action == "-":
                    self.energies[racer_idx] -= 1
                    if self.energies[racer_idx] < 0:
                        self.energies[racer_idx] = 0
                elif action == "=":
                    pass

        elif track == "+":
            for racer_idx in range(self.num_racers):
                self.energies[racer_idx] += 1
        elif track == "-":
            for racer_idx in range(self.num_racers):
                self.energies[racer_idx] -= 1
                if self.energies[racer_idx] < 0:
                    self.energies[racer_idx] = 0
        else:
            raise ValueError

        for racer_idx in range(self.num_racers):
            self.scores[racer_idx] += self.energies[racer_idx]

        self.segments_finished += 1

    def runRace(self, rounds, progress_bar=False):

        if progress_bar:
            partitions = 50
            partitions_done = -1

        for round in range(rounds):
            if progress_bar:
                progress = partitions * round/rounds

                if progress > partitions_done + 1:
                    partitions_done += 1
                    print(f"|{'*'*partitions_done}{' '*(partitions-partitions_done)}|  {round}/{rounds} rounds")

            for segment in self.track:
                self.runSegment(segment)



    def ranking_str(self):
        ranking = ""

        results = self.scores.copy()
        results.sort(reverse=True)

        for result in results:
            racer_id = self.scores.index(result)
            ranking += self.racers[racer_id]

        return ranking

    def ranking_list(self):
        ranking = []

        results = self.scores.copy()
        results.sort(reverse=True)

        for result in results:
            racer_id = self.scores.index(result)
            ranking.append(self.racers[racer_id])

        return ranking


def generateRacePlans(generated_racers: list, current_permutation: list, remaining_actions: dict):
    """
    Recursive function
    if remaining_actions == empty:
        add current_permutation to generated_racers
        :return

    else:
        for each remaining action type:
            add action to current_permutation
            remove action from a **a copy of** remaining_actions
            call generateRacePlans with new current_permutation and the copied remaining_actions
    """

    if not remaining_actions:
        generated_racers.append(current_permutation)
        return

    else:
        possible_actions = [possible_action for possible_action in remaining_actions if
                            remaining_actions[possible_action] > 0]
        for possible_action in possible_actions:
            new_permutation = current_permutation.copy()
            new_permutation.append(possible_action)

            new_remaining_actions = remaining_actions.copy()
            new_remaining_actions[possible_action] -= 1
            if new_remaining_actions[possible_action] == 0:
                new_remaining_actions.pop(possible_action)

            generateRacePlans(generated_racers, new_permutation, new_remaining_actions)
    pass


for part in [1, 2, 3]:

    race = Race()
    with open(f"Input_{part}", 'r') as _file:
        _lines = _file.readlines()

        for line in _lines:
            if line == "\n":
                break

            race.addRacer(line.replace(":", ",").removesuffix("\n").split(","))

        race.addTrack([line.removesuffix("\n") for line in _lines[_lines.index("\n") + 1:]])

    if part == 1 or part == 2:
        race.runRace(10)
        answer = race.ranking_str()
    elif part == 3: # quite slow, but brute force worked
        # generate race plans
        opponent_plan = race.plans[0]
        race_plans = []
        possible_actions = {action: opponent_plan.count(action) for action in ["+", "-", "="]}
        generateRacePlans(race_plans, [], possible_actions)

        race_plans.remove(race.plans[0])

        for plan_id, race_plan in enumerate(race_plans):
            race.addRacer([plan_id] + race_plan)

        race.runRace(2024, progress_bar=True)
        answer = race.ranking_list().index('A')

    print(f"Part {part}: {answer}", end="\n\n\n")
