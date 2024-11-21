monster_map = {
    "A":0,
    "B":1,
    "C":3,
    "D":5,
    "x":0
}

# Parts Challenge_1 - 3
for part in range(1,4):
    _file = open(f"Input_{part}", 'r')
    monsters = _file.readline()

    group_size = part
    potion_sum = 0

    groups = [monsters[i:i+group_size] for i in range(0, len(monsters), group_size)]
    for group in groups:
        for monster in group:
            potion_sum += monster_map[monster]

        # strength by numbers correction
        num_monsters = group_size - group.count("x")
        potion_sum += num_monsters*(num_monsters-1)

    print(f"part {part}: {potion_sum}")
    _file.close()